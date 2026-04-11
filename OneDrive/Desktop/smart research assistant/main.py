from pdf_loader import load_pdf, chunk_text
from retriever import build_index, search

file_path = "your_pdf_name.pdf"

print("Loading pdf")
text = load_pdf(file_path)

print("Splitting into chunks")
chunks = chunk_text(text)
print(f"Total chunks created: {len(chunks)}")

print("Building search index")
index, embeddings = build_index(chunks)

print("Searching now")
query = "What is the main topic of this paper?"
results = search(query, index, chunks)

print("Top 3 relevant chunks: ")
for i, reult in enumerate(results):
    print(f"Result {i+1}: ")
    print(result)
    