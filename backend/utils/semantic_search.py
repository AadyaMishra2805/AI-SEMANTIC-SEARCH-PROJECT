import chromadb
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Load collection
collection = client.get_collection(name="pdf_documents")

# User query
query = "How AI helps healthcare"

# Convert query into embedding
query_embedding = model.encode(query).tolist()

# Perform similarity search
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

# Print results
print("\nQuery:\n")
print(query)

print("\nTop Matching Chunks:\n")

for i, doc in enumerate(results['documents'][0]):
    print(f"\n--- Result {i+1} ---\n")

    print("Document:")
    print(doc)

    print("\nMetadata:")
    print(results['metadatas'][0][i])