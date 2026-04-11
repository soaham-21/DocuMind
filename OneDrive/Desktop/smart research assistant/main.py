from pdf_loader import load_pdf, chunk_text
from retriever import build_index, search

file_path = "attention-is-all-you-need.pdf"

print("Loading pdf")
text = load_pdf(file_path)

print("Splitting into chunks")
chunks = chunk_text(text)
print(f"Total chunks created: {len(chunks)}")

print("Building search index")
index, embeddings = build_index(chunks)

print("\nReady! Ask a question (type 'quit' to stop):")

while True:
    query = input("\nYour question: ")
    if query.lower() == "quit":
        break
    results = search(query, index, chunks, top_k=3)
    print("\n--- Top 3 relevant chunks ---")
    for i, result in enumerate(results):
        print(f"\nResult {i+1}:")
        print(result[:500])
        print("-" * 40)
    