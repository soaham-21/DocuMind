# DocuMind

Ask questions about any PDF in plain English and get AI-powered answers with citations.
If the answer isn't in the document, Grimoire automatically searches the web.

## Features

* Upload any PDF and interact with it conversationally
* Answers include citations pointing to the exact source text
* Semantic search over the document using embeddings and FAISS
* Automatic web search fallback when the document lacks the answer
* Clear separation between document-grounded answers and web results
* Simple Gradio interface for local use

---

## Tech Stack

* Python
* Sentence Transformers (embeddings)
* FAISS (vector similarity search)
* Google Gemini API (LLM)
* PyMuPDF (PDF parsing)
* DuckDuckGo Search (web fallback tool)
* Gradio (UI)

---

## How It Works

1. The PDF is parsed and split into meaningful text chunks
2. Each chunk is converted into an embedding and stored in a FAISS vector index
3. When you ask a question:

   * The most relevant chunks are retrieved via semantic similarity
   * These chunks are passed to the LLM as context
   * If the context is insufficient, the agent triggers a web search
4. The final answer includes citations and indicates the source of information

---

## Running Locally

1. Clone the repository

   ```bash
   git clone https://github.com/soaham-21/DocuMind
   cd DocuMind
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Gemini API key

   ```
   GEMINI_API_KEY=your_key_here
4. Run the app
   python app.py
5. Open http://localhost:7860 in your browser

## What I learned
- How RAG pipelines work in practice
- How embeddings and vector search enable semantic search
- How to build agentic fallback logic
- How to go from a terminal script to a deployed web app