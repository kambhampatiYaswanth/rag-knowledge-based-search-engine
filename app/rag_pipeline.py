from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# load once
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def create_vector_store(chunks):
    return FAISS.from_documents(chunks, embeddings)


def retrieve_documents(vector_store, query):
    retriever = vector_store.as_retriever(
        search_type="mmr",  # 🔥 better than similarity
        search_kwargs={"k": 4}
    )
    return retriever.invoke(query)