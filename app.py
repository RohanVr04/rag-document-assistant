from flask import Flask, redirect, render_template, request


from rag_utils import (
    extract_text,
    create_chunks,
    create_embeddings,
    create_faiss_index,
    retrieve_chunks,
    generate_answer
)

app = Flask(__name__)


chunks = None
faiss_index = None
embedding_model = None


# Home Route

@app.route("/")
def home():
    return render_template("home.html")


# Upload Route
@app.route("/upload", methods=["POST"])
def upload():
    global chunks, faiss_index, embedding_model

    file = request.files["file"]

    if file and file.filename != "":
        text = extract_text(file)

        chunks = create_chunks(text)

        embedding_model, embeddings = create_embeddings(chunks)

        faiss_index = create_faiss_index(embeddings)

        return redirect("/chat")

    return render_template(
        "home.html",
        message="No file uploaded!"
    )

# Chat Route

@app.route("/chat")
def chat():

    return render_template(
        "chat.html"
    )


# Ask Route
@app.route("/ask", methods=["POST"])
def ask():
    global chunks, faiss_index, embedding_model
    if faiss_index is None:
        return redirect("/")

    query = request.form["query"]

    if not chunks or not faiss_index or not embedding_model:
        return render_template(
            "home.html",
            message="Please upload a document first!"
        )

    retrieved_chunks = retrieve_chunks(query, embedding_model, faiss_index, chunks)

    from dotenv import load_dotenv
    import os

    load_dotenv()

    API_KEY = os.getenv("GEMINI_API_KEY")

    answer, sources = generate_answer(query, retrieved_chunks, API_KEY)

    return render_template(
        "chat.html",
        query=query,
        answer=answer,
        sources=sources
    )

app.run()
