from uuid import UUID, uuid4

from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_community.document_loaders.youtube import YoutubeLoader
from langchain_core.documents import Document


def determine_loader(url: str) -> BaseLoader:
    if ".pdf" in url:
        return PyPDFLoader(url)
    if "youtube" in url or "youtu.be" in url:
        return YoutubeLoader.from_youtube_url(url, add_video_info=False, language=["en", "pt"], translation="en")
    
    return WebBaseLoader(url)

class Loader:
    def __init__(self, url: str):
        self.loader = determine_loader(url)

    def load(self) -> tuple[list[Document], UUID]:
        return self.loader.load(), uuid4()
