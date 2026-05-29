from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
if __name__ == "__main__":
    
    #docs = load_all_documents("Data")
    store=FaissVectorStore("faiss_store")
    store.load()
   # print(store.query("entrepreneurship",top_k=3))
    rag_search = RAGSearch()
    query = "What is Entrepreneur?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
    #store.build_from_documents(docs)
    # pipeline = EmbeddingPipeline()
    # chunks=pipeline.chunk_documents(docs)
    # chunkvectors=pipeline.embed_chunks(chunks)
    # print(chunkvectors)
    # #print(store.query("What is attention mechanism?", top_k=3))
