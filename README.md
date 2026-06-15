# 📚 DocMind AI RAG

An AI-powered PDF Question Answering System built using **Retrieval-Augmented Generation (RAG)**, **FAISS**, **Sentence Transformers**, **Gemini AI**, and **Flask**.

DocMind AI allows users to upload PDF documents and ask natural language questions about their content. The application retrieves the most relevant document sections using semantic search and generates context-aware answers using Google's Gemini model.

---

## 🚀 Features

* 📄 Upload and process PDF documents
* ✂️ Recursive text chunking for better context preservation
* 🧠 Semantic embeddings using Sentence Transformers
* 🔍 Fast similarity search using FAISS
* 🤖 AI-generated answers using Gemini AI
* 📚 Source chunk retrieval and display
* 🎨 Modern and responsive Flask UI
* 🔐 Secure API key management using `.env`

---

## 🏗️ Project Architecture

```text
PDF Document
      │
      ▼
Text Extraction
      │
      ▼
Recursive Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Index
      │
      ▼
Similarity Search
      │
      ▼
Relevant Context Retrieval
      │
      ▼
Gemini AI
      │
      ▼
Generated Answer + Sources
```

---

## ⚙️ Tech Stack

### Backend

* Python
* Flask

### NLP & RAG

* Sentence Transformers
* FAISS
* Recursive Text Chunking

### LLM

* Gemini 2.5 Flash

### PDF Processing

* PyPDF2

### Frontend

* HTML
* CSS

### Environment Management

* python-dotenv

---

## 📂 Project Structure

```text
docmind-ai-rag/
│
├── app.py
├── rag_utils.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── home.html
│   └── chat.html
│
└── static/
```

---

## 🧠 How It Works

### 1. PDF Upload

The user uploads a PDF document through the web interface.

### 2. Text Extraction

Text is extracted from the PDF using PyPDF2.

### 3. Recursive Chunking

The extracted text is split into overlapping chunks using Recursive Character Text Splitting.

Example:

```text
Chunk 1 → Words 1-300
Chunk 2 → Words 250-550
Chunk 3 → Words 500-800
```

This overlap helps preserve context between chunks.

### 4. Embedding Generation

Each chunk is converted into a dense vector representation using:

```text
all-MiniLM-L6-v2
```

from Sentence Transformers.

### 5. Vector Storage

The embeddings are stored in a FAISS vector index.

### 6. Query Processing

When a user asks a question:

* The query is embedded
* Similar chunks are retrieved from FAISS
* Top relevant chunks are selected

### 7. Answer Generation

Retrieved chunks are passed as context to Gemini AI, which generates a final answer.

### 8. Source Display

The chunks used to generate the answer are displayed as sources.

---

## 📌 Why RAG?

Traditional LLMs rely solely on their training data.

RAG improves accuracy by retrieving relevant information from external documents before generating an answer.

Benefits:

* Reduced hallucination
* More accurate answers
* Domain-specific knowledge
* Uses latest uploaded documents

---

## 📸 Screenshots

### Home Page




screenshots/home.png


### Chat Interface


screenshots/chat.png


### Answer Generation


screenshots/answer.png


---

## 🛠️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/docmind-ai-rag.git

cd docmind-ai-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from Google AI Studio.

---

## ▶️ Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📝 Example Usage

1. Upload a PDF document.
2. Wait for processing to complete.
3. Ask a question.

Example:

```text
What is Deep Learning?
```

Answer:

```text
Deep Learning is a subset of Machine Learning that uses
neural networks with multiple layers.
```

Sources:

```text
Source 1
Source 2
Source 3
```

---

## 🎯 Learning Outcomes

This project helped demonstrate:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embedding Models
* Prompt Engineering
* Large Language Model Integration
* Flask Deployment
* Environment Variable Management

---

## 🔮 Future Improvements

* Multi-PDF support
* Chat history
* ChromaDB integration
* Pinecone integration
* User authentication
* Document management dashboard
* Streaming responses
* Source highlighting
* PDF page references
* Docker deployment

---

## 👨‍💻 Author

**Rohan Verma**

M.Tech (Data Science & AI)

Passionate about Artificial Intelligence, Machine Learning, Deep Learning, NLP, and Building AI-Powered Applications.

---

## ⭐ If you found this project useful

Consider giving the repository a star.
