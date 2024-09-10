from typing import List

from config import anthropic_api_key
from haystack import Pipeline
from haystack.components.builders import ChatPromptBuilder
from haystack.components.generators.utils import print_streaming_chunk
from haystack.components.readers import ExtractiveReader
from haystack.dataclasses import ChatMessage, ExtractedAnswer
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
from store_interface import Retriever

messages = [
    ChatMessage.from_system(
        "You are a prompt expert who answers questions based on the given documents."
    ),
    ChatMessage.from_user(
        "Here are the documents:\n"
        "{% for d in documents %} \n"
        "    {{d.content}} \n"
        "{% endfor %}"
        "\nAnswer: {{query}}"
    ),
]

anthropic_chat_generator = AnthropicChatGenerator(
    api_key=anthropic_api_key,
    model="claude-3-haiku-20240307",
    streaming_callback=print_streaming_chunk,
)


rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", Retriever(top_k=3))
rag_pipeline.add_component("prompt_builder", ChatPromptBuilder(template=messages))
rag_pipeline.add_component("llm", anthropic_chat_generator)
rag_pipeline.connect("retriever", "prompt_builder")
rag_pipeline.connect("prompt_builder.prompt", "llm.messages")


def run_rag_pipeline(query: str) -> List[ChatMessage]:
    documents = rag_pipeline.run(
        data={
            "retriever": {"query": query},
            "prompt_builder": {"template_variables": {"query": query}},
        }
    )
    # return documents["prompt_builder"]["prompt"]
    return documents["llm"]["replies"]


reader_pipeline = Pipeline()
reader_pipeline.add_component("retriever", Retriever(top_k=3))
reader_pipeline.add_component("reader", ExtractiveReader(top_k=3))
reader_pipeline.connect("retriever", "reader")


def run_reader_pipeline(query: str) -> List[ExtractedAnswer]:
    documents = reader_pipeline.run(
        data={
            "retriever": {"query": query},
            "reader": {"query": query},
        }
    )
    return documents["reader"]["answers"]
