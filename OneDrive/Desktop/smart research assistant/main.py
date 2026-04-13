from pdf_loader import load_pdf, chunk_text
from retriever import build_index, search
from answerer import get_answer_with_citation, ask_llm, build_prompt
from web_search import search_web, answer_from_web

file_path = "attention-is-all-you-need.pdf"

print("Loading PDF...")
text = load_pdf(file_path)

print("Splitting into chunks...")
chunks = chunk_text(text)
print(f"Total chunks created: {len(chunks)}")

print("Building search index...")
index, embeddings = build_index(chunks)

print("\nGrimoire is ready! Ask anything. (type 'quit' to stop)\n")

while True:
    query = input("Your question: ")
    
    if query.lower() == "quit":
        break
    
    print("\nSearching document...")
    relevant_chunks = search(query, index, chunks, top_k=3)
    
    print("Asking AI...")
    answer, citation = get_answer_with_citation(query, relevant_chunks)
    
    if answer is None:
        print("Answer not found in document. Searching the web...")
        web_chunks = search_web(query)
        web_context = answer_from_web(query, web_chunks)
        
        web_prompt = build_prompt(query, web_chunks)
        web_answer = ask_llm(web_prompt)
        
        print("\n" + "="*50)
        print(f"Answer: {web_answer}")
        print(f"Source: Web search (not in your document)")
        print("="*50 + "\n")
    
    else:
        print("\n" + "="*50)
        print(f"Answer: {answer}")
        print(f"{citation}")
        print("="*50 + "\n")