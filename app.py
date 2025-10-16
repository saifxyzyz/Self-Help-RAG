from data_loader import load_all_documents
from vectorstore import FaissVectorStore
from search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)  # comment this line after executing app.py once
    # store.load()  # uncomment this line after running app.py once
    print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    query = "what should I do when feeling low?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
