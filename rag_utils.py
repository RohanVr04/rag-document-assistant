import numpy as np
import faiss

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai


# Extracting text from PDF
def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


# Creating CHUNKS using RecursiveCharacterTextSplitter

def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks

# Creating Embeddings

def create_embeddings(chunks):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(chunks)

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    return model, embeddings


# Vector Database

def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


def retrieve_chunks(query, model, index, chunks, k=3):

    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding, dtype=np.float32)

    distances, indices = index.search(query_embedding, k)

    retrieved_chunks = []

    for i in indices[0]:
        retrieved_chunks.append(chunks[i])

    return retrieved_chunks


def generate_answer(query, retrieved_chunks, api_key):

    context = ""

    for i in range(len(retrieved_chunks)):
        context += f"Source {i+1}\n{retrieved_chunks[i]}\n\n"

    prompt = f"""
    You are a helpful AI assistant.

    Answer the question using only the provided context.

    If the answer exists in the context, explain it in 2-3 sentences.

    When using information, mention the source number.

    Context:
    {context}

    Question:
    {query}
    """

    client = genai.Client(
        api_key=api_key
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip(), [chunk.strip() for chunk in retrieved_chunks]