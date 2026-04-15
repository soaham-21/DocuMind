import os
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(query, chunks):
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Chunk {i+1}]:\n{chunk}\n\n"

    prompt = f"""You are a helpful research assistant.
Use ONLY the following chunks from a document to answer the question. If the answer is not in the chunks, say exactly: NOT_IN_DOCUMENT
Do not make up any information.

Document chunks:
{context}

Question: {query}
Answer clearly and concisely in 3-4 sentences."""
    return prompt

def ask_llm(prompt):
    models = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
    
    for model_name in models:
        try:
            completion = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1024,
            )
            return completion.choices[0].message.content.strip()
        
        except Exception as e:
            
            if "429" in str(e) and model_name != models[-1]:
                print(f"Rate limit hit on {model_name}, switching to fallback...")
                continue
            return f"Error: {str(e)}"

def get_answer_with_citation(query, chunks):
    prompt = build_prompt(query, chunks)
    answer = ask_llm(prompt)

    if not answer or "NOT_IN_DOCUMENT" in answer:
        return None, None
    
    citation = "Source: Document Chunks"
    return answer, citation