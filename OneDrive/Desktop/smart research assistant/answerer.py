import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"

headers = {
    "Authorization" : f"Bearer {HF_TOKEN}"
}

def build_prompt(query, chunks):
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Chunk {i+1}]:\n{chunk}\n\n"

    prompt = f"""<s>[INST] You are a helpful research assistant.isinstance
Use ONLY the following chunks from a document to answer the question.
If the answer is not in the chunks, say exactly: "NOT_IN_DOCUMENT"
Do not make up any information.
Document chunks: {context}
Question : {query}
Answer clearly and concisely in 3-4 sentences. [/INST]"""
    return prompt

def ask_llm(prompt):
    payload = {
        "inputs" : prompt,
        "parameters" : {
            "max_new_tokens" : 300,
            "temperature" : 0.3,
            "return_full_text" : False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"API Error: {response.status_code} - {response.text}"
    result = response.json()
    answer = result[0]["generated_text"]
    return answer.strip()

def get_answer_with_citation(query, chunks):
    prompt = build_prompt(query, chunks)
    answer = ask_llm(prompt)

    if "NOT_IN_DOCUMENT" in answer:
        return None, None
    best_chunk_index = 0
    citation = f"Source : Document, chunk {best_chunk_index+1}"
    return answer, citation

