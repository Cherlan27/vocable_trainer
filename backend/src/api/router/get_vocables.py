from fastapi import APIRouter

from backend.src.services.voc_extracter import VocExtracter
from backend.src.models.api_models import Word

WORD_TYPE = "noun"

router = APIRouter()

@router.get("/cards",
    response_model=Word
)
async def get_vocables():
    """
    Get a random vocable of the specified type.

    Returns:
        Word: A Word object containing the French word and its tags.
    """
    extractor = VocExtracter()

    expression = extractor.extract_one_word(WORD_TYPE)

    word = Word(
        french=expression.get("form", ""),
        tag=expression.get("tags", [])
    )
    return word
