import os

from fastapi import APIRouter, Depends
from models.api_models import TopicRequest
from services.deps import get_voc_generator

URL = os.getenv("llm_url")
router = APIRouter()


@router.post("/new_vocables")
async def generate_new_vocables(
    request: TopicRequest, voc_generator=Depends(get_voc_generator)
):
    response = voc_generator.generate_vocables_for_topic(request.topic)

    return {"vocables": response}
