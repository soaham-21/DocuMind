# DocuMind

Ask questions about any PDF in plain English and get AI-powered answers with clear citations.
If the answer isn’t in the document, DocuMind automatically searches the web and tells you which parts came from the document vs. the web.

DocuMind is built as a complete Retrieval-Augmented Generation (RAG) pipeline with an agentic fallback workflow.

---

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
* Groq API (LLM)
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
   git clone https://github.com/soaham-21/DocuMind.git
   cd DocuMind
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Gemini API key

   ```
   GROQ_API_KEY=your_key_here
   ```

4. Start the application

   ```bash
   python website.py
   ```

5. Open `http://localhost:7860` in your browser

---

## Example Questions to Try

* “Summarize the introduction section”
* “What methodology does the author use?”
* “Explain this paper in simple terms”
* “What is reinforcement learning?” (triggers web fallback if not in the PDF)

---

## What I Learned Building This

* How RAG systems work beyond theory
* How embeddings and vector search enable semantic retrieval
* How to design agentic logic that decides when to use external tools
* How to turn an ML pipeline into a usable web application

---

## Why This Project Matters

DocuMind demonstrates a production-style RAG architecture with tool-calling behavior. It reflects practical skills in retrieval systems, LLM grounding, and building interactive ML applications.

---

## Future Improvements

* Support for multiple PDFs
* Persistent vector storage
* Highlight cited text directly in the document view
* Streaming responses for better UX

---