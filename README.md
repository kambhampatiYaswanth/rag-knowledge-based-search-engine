# 📄 RAG-Based Knowledge Base Search

## 🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) application that allows users to:

* Upload a PDF document
* Ask questions about the document
* Receive accurate answers using AI

---

## 🧠 Tech Stack

* FastAPI (Backend)
* FAISS (Vector Database)
* LangChain (RAG Pipeline)
* Google Gemini API (LLM)
* HTML/CSS/JS (Frontend)

---

## ⚙️ Features

* Upload any PDF
* Semantic search using embeddings
* AI-generated answers
* Chat-style interface

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start backend

```bash
python -m uvicorn app.api:app
```

### 3. Start frontend

```bash
cd frontend
python -m http.server 5500
```

### 4. Open in browser

```
http://localhost:5500/index.html
```


## 👨‍💻 Author

Kambhampati Yaswanth Sai Kishore
