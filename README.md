# DocuMind

Ask questions about any PDF in plain English and get AI-powered answers with citations.
If the answer isn't in the document, DocuMind automatically searches the web.

## Features
- Upload any PDF and chat with it
- Answers include citations showing which part of the document was used
- Automatic web search fallback when the document doesn't have the answer
- Built with RAG (Retrieval Augmented Generation)

## Tech Stack
- Python
- Sentence Transformers (embeddings)
- FAISS (vector search)
- Google Gemini API (LLM)
- Gradio (UI)
- DuckDuckGo Search (web fallback)

## How to run locally

1. Clone this repo
2. Install dependencies
   pip install -r requirements.txt
3. Create a .env file with your Gemini API key
   GEMINI_API_KEY=your_key_here
4. Run the app
   python app.py
5. Open http://localhost:7860 in your browser

## What I learned
- How RAG pipelines work in practice
- How embeddings and vector search enable semantic search
- How to build agentic fallback logic
- How to go from a terminal script to a deployed web app
