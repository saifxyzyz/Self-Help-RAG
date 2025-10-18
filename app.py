from data_loader import load_all_documents
from vectorstore import FaissVectorStore
from search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)  # comment this line after executing app.py once
    store.load()  # uncomment this line after running app.py once
    # print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    while True:
        # Get user input
        query = input("\nQuery: ")
        
        # Check for exit commands
        if query.lower() in ['quit', 'exit', 'bye']:
            print("Session ended. Goodbye!")
            break
        
        # Ensure query is not empty
        if not query.strip():
            continue

        try:
            # Perform search and summarization (single inference, no history used)
            # The original query is passed directly as the standalone query.
            print(f"[INFO] Processing query: '{query}'")
            summary = rag_search.search_and_summarize(query, top_k=3)
            
            # Print the result
            print("--- Summary ---")
            print(summary)
            print("---------------")

        except Exception as e:
            # Catch any errors during the retrieval or generation steps
            print(f"[ERROR] An unexpected error occurred: {e}")
            print("Please try your query again.")
