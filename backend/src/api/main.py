from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.src.api.router.get_vocables import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api", tags=["vocables"])
