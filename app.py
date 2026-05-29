
import streamlit as st

st.set_page_config(page_title="RAG App")

st.title("🤖 RAG Search Assistant")

# Test UI first
st.write("Streamlit is working!")

try:
    from src.vectorstore import FaissVectorStore
    from src.search import RAGSearch

    st.success("Modules imported successfully!")

    # Load FAISS
    @st.cache_resource
    def load_rag():
        store = FaissVectorStore("faiss_store")
        store.load()
        return RAGSearch()

    rag_search = load_rag()

    st.success("FAISS store loaded!")

    # Input
    query = st.text_input("Ask a question")

    top_k = st.slider("Top K", 1, 10, 3)

    if st.button("Search"):

        if query.strip() == "":
            st.warning("Enter a question")

        else:
            with st.spinner("Searching..."):

                result = rag_search.search_and_summarize(
                    query=query,
                    top_k=top_k
                )

                st.subheader("Answer")
                st.write(result)

except Exception as e:
    st.error(f"Error occurred: {e}")

