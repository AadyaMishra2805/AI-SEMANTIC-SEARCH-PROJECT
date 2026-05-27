import chromadb

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.pdf_loader import load_pdf


# Load PDF text
text = load_pdf("data/sample.pdf")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_text(text)

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(chunks).tolist()

# Initialize ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Create collection
collection = client.get_or_create_collection(name="pdf_documents")

# Create metadata
metadatas = []

for i in range(len(chunks)):
    metadatas.append({
        "chunk_id": i,
        "source": "sample.pdf",
        "topic": "AI"
    })

# Store in ChromaDB
collection.add(
    documents=chunks,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=[f"id{i}" for i in range(len(chunks))]
)

print("Embeddings + Metadata stored successfully!")