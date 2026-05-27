from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.text_chunker import chunk_text

# Load PDF text
text = load_pdf("data/sample.pdf")

# Create chunk splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

# Split text into chunks
chunks = text_splitter.split_text(text)

# Print chunks
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---\n")
    print(chunk)