from fastapi import APIRouter
from models.api_models import Word

WORD_TYPE = "noun"

router = APIRouter()


@router.get("/cards", response_model=Word)
async def get_vocables():
    pass
