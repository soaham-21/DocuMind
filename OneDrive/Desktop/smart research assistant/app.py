import gradio as gr
from pdf_loader import load_pdf, chunk_text
from retriever import build_index, search
from answerer import get_answer_with_citation, ask_llm, build_prompt
from web_search import search_web, answer_from_web

index = None
chunks = None

def process_pdf(pdf_file):
    global index, chunks

    if pdf_file is None:
        return "Please upload a PDF file first."
    try:
        print("Loading PDF...")
        text = load_pdf(pdf_file.name)

        print("Chunking text...")
        chunks = chunk_text(text)

        print("Building index...")
        index, embeddingd = build_index(chunks)

        return f"PDF loaded succesfully! Created {len(chunks)} chunks. You can now ask questions. "
    
    except Exception as e:
        return f"error loading pdf: {str(e)}"

def answer_question(question):
    global index, chunks

    if index is None or chunks is None:
        return "Please upload a PDF first before asking questions."
    
    if not question.strip():
        return "Please type a question."
    
    try:
        relevant_chunks = search(question, index, chunks, top_k=3)
        answer, citation = get_answer_with_citation(question, relevant_chunks)

        if answer is None:
            print("Not in document, searching web ....")
            web_chunks = search_web(question)
            web_prompt = build_prompt(question, web_chunks)
            web_answer = ask_llm(web_prompt)

            return f"Answer:\n{web_answer}\n\nSource: Web search (not found in your document)"
        
        return f"Answer:/n{answer}/n/n{citation}"
    
    except Exception as e:
        return f"Error: {str(e)}"
    
with gr.Blocks(title="Grimoire") as app:

    gr.Markdown("# Grimoire")
    gr.Markdown("Upload any pdf and ask questions about it in plain English.")

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(
                label = "Upload your PDF",
                file_types= [".pdf"]
            )

            upload_btn =  gr.Button(
                "Load PDF",
                variant = "primary"
            )

            upload_status = gr.Textbox(
                label="Status",
                interactive=False,
                lines=2
            )

        with gr.Column(scale=2):
            question_input = gr.Textbox(
                label="Your question",
                placeholder="e.g. What is the main contribution of this paper?",
                lines=3
            )

            ask_btn = gr.Button(
                "Ask Grimoire",
                variant="primary"
            )

            answer_output = gr.Textbox(
                label="Answer",
                interactive=False,
                lines=10
            )

    upload_btn.click(
        fn=process_pdf,
        inputs=pdf_input,
        outputs=upload_status
    )

    ask_btn.click(
        fn=answer_question,
        inputs=question_input,
        outputs=answer_output
    )

    question_input.submit(
        fn=answer_question,
        inputs=question_input,
        outputs=answer_output
    )

app.launch()