from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.embed_chunks import embed_chunks


# Load PDF text
text = load_pdf("data/sample.pdf")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_text(text)

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(chunks)

# Print results
print("Total Chunks:", len(chunks))
print("Embedding Shape:", embeddings.shape)

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nFirst Embedding Vector (first 10 values):\n")
print(embeddings[0][:10])