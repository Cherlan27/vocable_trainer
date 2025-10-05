import random

from fastapi import APIRouter

from backend.src.services.voc_extracter import VocExtracter
from backend.src.models.api_models import Word

WORD_TYPE = "noun"

router = APIRouter()

@router.get("/cards",
    response_model=Word
)
async def get_vocables():
    extractor = VocExtracter()

    french_df = extractor.extract(WORD_TYPE)
    word_counts = int(random.uniform(0, french_df.shape[0]))

    expression = french_df.iloc[word_counts]

    if isinstance(expression["tags"], float):
        expression["tags"] = []

    word = Word(
        french=expression["form"],
        tag=expression["tags"]
    )
    return word
