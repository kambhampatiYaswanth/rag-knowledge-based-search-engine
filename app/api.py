from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import shutil

from app.ingest import load_documents, split_documents
from app.rag_pipeline import create_vector_store, retrieve_documents
from app.llm import get_llm_response
import os
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_store = None  # 🔥 GLOBAL

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "RAG API is running 🚀"}


# ✅ Upload PDF
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    global vector_store

    os.makedirs("data", exist_ok=True)  # ✅ ensure folder exists

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    docs = load_documents(file_path)
    chunks = split_documents(docs)

    vector_store = create_vector_store(chunks)

    return {"message": "✅ File uploaded successfully"}
# ✅ Query
@app.post("/query")
def query_rag(request: QueryRequest):
    global vector_store

    if vector_store is None:
        return {"answer": "⚠️ Please upload a document first."}

    query = request.query

    # 🔍 retrieve relevant chunks
    retrieved_docs = retrieve_documents(vector_store, query)

    if not retrieved_docs:
        return {"answer": "No relevant content found."}

    # 🧠 build context
    context = "\n\n".join([
        doc.page_content for doc in retrieved_docs[:2]
    ])

    # 🎯 strong prompt
    prompt = f"""
    You are a strict document question-answering system.

    Rules:
    - Answer ONLY from the context
    - Do NOT guess
    - Do NOT include extra information
    - If not found, say "Not found"

    Context:
    {context}

    Question: {query}

    Answer (short, clean, exact):
    """

    answer = get_llm_response(prompt)

    return {"answer": answer}