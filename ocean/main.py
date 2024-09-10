from typing import List

import gradio as gr
from haystack.dataclasses import ChatMessage, ExtractedAnswer
from llm_integration import run_rag_pipeline, run_reader_pipeline
from store_interface import document_store, run_indexing_pipeline


def index_data() -> None:
    if document_store.count_documents() == 0:
        print("Indexing data...")
        run_indexing_pipeline()
    else:
        print("Data already indexed")


def extracted_answer_display(extracted_answer: ExtractedAnswer) -> str:
    answer = f"answer = {extracted_answer.data}"
    score = f"score = {extracted_answer.score}"
    if extracted_answer.document:
        content = extracted_answer.document.content
        flat_content = content.replace("\n", " ").replace("\r", "")
        document = f"document = {flat_content}"
        url = f"url = {extracted_answer.document.meta['url']}"
    else:
        document = "document = None"
        url = "url = None"

    return "\n".join([answer, score, document, url])


def extracted_answers_display(extracted_answers: List[ExtractedAnswer]) -> str:
    extracted_answer_strings = [
        extracted_answer_display(extracted_answer)
        for extracted_answer in extracted_answers[:-1]
    ]
    return "\n\n".join(extracted_answer_strings)


def reader_chatbot(message: str, history: str) -> str:
    extracted_answer = run_reader_pipeline(message)
    return extracted_answers_display(extracted_answer)


def rag_chatbot(message: str, history: str) -> str:
    chat_messages = run_rag_pipeline(message)
    return "\n".join([str(chat_message.content) for chat_message in chat_messages])


if __name__ == "__main__":
    ocean = gr.ChatInterface(
        fn=rag_chatbot,
        title="Ask Ocean!",
        description="Welcome to Online Chatbot for Effective Altruism Navigation (OCEAN). This chatbot is designed to answer your questions based on EA resources.",
    )

    ocean.launch()
