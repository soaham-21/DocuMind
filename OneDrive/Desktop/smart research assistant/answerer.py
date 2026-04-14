import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def build_prompt(query, chunks):
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Chunk {i+1}]:\n{chunk}\n\n"

    prompt = f"""You are a helful research assistant.
Use ONLY the following chunks from a document to answer the question. If the answer is not in the chunks, say exactly: NOT_IN_DOCUMENT
Do not make up any information.
Document chunks:
{context}
Question : {query}
Answer clearly and concisely in 3-4 sentences."""
    return prompt

def ask_llm(prompt):
    try:
        response =  model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_answer_with_citation(query, chunks):
    prompt = build_propmt(query,chunks)
    answer = ask_llm(prompt)

    if "NOT_IN_DOCUMENT" in answer:
        return None, None
    
    citation = f"Source: Document, Chunk 1"
    return answer, citation