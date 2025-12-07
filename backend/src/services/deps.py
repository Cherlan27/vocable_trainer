import os

from src.services.llm_service.llm_handler import LLMHandler
from src.services.llm_service.voc_generation import VocGenerator


def get_llm_service() -> LLMHandler:
    URL = os.getenv("llm_url")
    return LLMHandler(url=URL)


def get_voc_generator() -> VocGenerator:
    llm_service = get_llm_service()
    return VocGenerator(llm=llm_service)
