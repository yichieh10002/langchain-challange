try:
    from langchain_community.document_loaders.web_base import WebBaseLoader
except ImportError:
    # 舊版本
    from langchain_community.document_loaders import WebBaseLoader


# 抓取網頁內容
def scrape_webpage(url: str) -> str:
    loader = WebBaseLoader(url)

    # load() → 會回傳 List[Document]
    docs = loader.load()
    return docs[0].page_content
