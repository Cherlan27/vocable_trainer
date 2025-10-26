import os

from fastapi import APIRouter

from backend.src.models.api_models import ChatMessage, PromptData
from backend.src.services.llm_service import LLMHandler

URL = os.getenv("llm_url")
router = APIRouter(prefix="/generate")


@router.post("/new_vocables")
async def generate_new_vocables(
    topic: str,
):
    llm = LLMHandler(URL)
    response = llm.generate(
        PromptData(
            messages=[ChatMessage(role="user", content=topic)],
            max_new_tokens=1000,
        )
    )

    return {"generated_vocables": response}
