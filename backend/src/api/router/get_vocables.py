from fastapi import APIRouter

WORD_TYPE = "noun"

router = APIRouter()


@router.get("/cards")
async def get_vocables():
    return None
