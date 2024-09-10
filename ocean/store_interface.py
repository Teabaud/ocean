from typing import Any, Dict

from config import data_urls, persist_path
from haystack import Pipeline
from haystack.components.converters import HTMLToDocument
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.document_stores.types import FilterPolicy
from haystack_integrations.components.retrievers.chroma import ChromaQueryTextRetriever
from haystack_integrations.document_stores.chroma import ChromaDocumentStore

document_store = ChromaDocumentStore(
    persist_path=str(persist_path),
    embedding_function="default",
)


fetcher = fetcher = LinkContentFetcher()
converter = HTMLToDocument()
splitter = DocumentSplitter(split_by="sentence", split_length=10)
writer = DocumentWriter(document_store)
cleaner = DocumentCleaner(ascii_only=True)


class Retriever(ChromaQueryTextRetriever):
    def __init__(
        self,
        filters: Dict[str, Any] | None = None,
        top_k: int = 10,
        filter_policy: str | FilterPolicy = FilterPolicy.REPLACE,
    ):
        super().__init__(document_store, filters, top_k, filter_policy)


indexing_pipeline = Pipeline()
indexing_pipeline.add_component("fetcher", fetcher)
indexing_pipeline.add_component("converter", converter)
indexing_pipeline.add_component("cleaner", cleaner)
indexing_pipeline.add_component("splitter", splitter)
indexing_pipeline.add_component("writer", writer)

indexing_pipeline.connect("fetcher", "converter")
indexing_pipeline.connect("converter", "cleaner")
indexing_pipeline.connect("cleaner", "splitter")
indexing_pipeline.connect("splitter", "writer")


def run_indexing_pipeline():
    print("Indexing data...")
    indexing_pipeline.run({"fetcher": {"urls": data_urls}})
    print("Indexing complete!")
    print(f"Number of documents indexed: {document_store.count_documents()}")
