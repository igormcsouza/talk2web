from uuid import UUID, uuid4

from langchain_community.document_loaders.pdf import OnlinePDFLoader
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_core.documents import Document


class Loader:
    def __init__(self, url: str):
        self.loader = OnlinePDFLoader(url) if ".pdf" in url else WebBaseLoader(url)

    def load(self) -> tuple[list[Document], UUID]:
        return self.loader.load(), uuid4()
