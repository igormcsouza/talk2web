from os import getenv
from os.path import isdir, join
from uuid import UUID

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from pydantic.v1.types import SecretStr

load_dotenv()

FOLDER_PATH = "./docstore"
embeddings = OpenAIEmbeddings(api_key=SecretStr(getenv("OPENAI_API_KEY", "")))


def prepare_vector_store_from_local(key: UUID) -> FAISS:
    if not isdir(join(FOLDER_PATH, str(key))):
        raise Exception(f"Could not locate the given store: {key}")

    return FAISS.load_local(
        folder_path=join(FOLDER_PATH, str(key)),
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )


def prepare_vector_store(documents: list[Document], key: UUID) -> FAISS:
    chunks = RecursiveCharacterTextSplitter().split_documents(documents)
    docstore = FAISS.from_documents(chunks, embeddings)
    docstore.save_local(folder_path=join(FOLDER_PATH, str(key)))

    return docstore
