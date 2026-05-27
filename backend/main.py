from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import chromadb

from sentence_transformers import SentenceTransformer


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Load ChromaDB
client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="pdf_documents"
)


@app.get("/")
def home():

    return {
        "message": "Backend running successfully"
    }


@app.get("/search")
def search(query: str):

    # Generate embedding
    query_embedding = model.encode(
        query
    ).tolist()

    # Semantic search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results["documents"][0]

    return {
        "results": documents
    }