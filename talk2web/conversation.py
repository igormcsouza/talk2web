from typing import Literal

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import (
    create_history_aware_retriever,
)
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import RetrieverOutputLike
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI


class Conversation:
    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0.7):
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.history: list[BaseMessage] = [
            AIMessage(
                content="Hello! I'm Stuart. I've learned from the context you entered and can answer any question about that. How can I be helpful today?"
            )
        ]

    def update_temperature(self, temperature: float):
        self.llm = ChatOpenAI(temperature=temperature)

    def update_model(self, model: str):
        self.llm = ChatOpenAI(model=model)

    def add_context(self, context_base: FAISS):
        self.retriever = context_base.as_retriever()

    def add_message(self, actor: Literal["ai", "human"], content: str):
        message = None

        match actor:
            case "ai":
                message = AIMessage(content=content)

            case "human":
                message = HumanMessage(content=content)

        if message:
            self.history.append(message)

    def get_history(self) -> list[BaseMessage]:
        return self.history

    def _generate_retriever_chain(self) -> RetrieverOutputLike:
        prompt = ChatPromptTemplate.from_template(
            "<history>{history}</history>\n"
            "<question>{input}</question>\n"
            "According to the above conversation, generate a search query to look up for useful information for the conversation."
        )

        return create_history_aware_retriever(self.llm, self.retriever, prompt)

    def _generate_stuff_document_chain(self) -> Runnable:
        prompt = ChatPromptTemplate.from_template(
            "Given the context:\n"
            "<context>{context}</context>\n"
            "Answer the user question: <question>{input}</question>"
            "Be kind and respectful as you answer the user's question.\n"
        )

        return create_stuff_documents_chain(self.llm, prompt)

    def ask(self, question: str) -> str:
        rag_chain = create_retrieval_chain(
            self._generate_retriever_chain(),
            self._generate_stuff_document_chain(),
        )
        response = rag_chain.invoke(
            {
                "history": self.history,
                "input": question,
            }
        )

        return response.get(
            "answer", "Sorry, couldn't not answer your question."
        )
