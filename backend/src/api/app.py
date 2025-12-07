from fastapi import FastAPI
from src.api.router import generate_vocables_router, get_vocables_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Vocables API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get_vocables_router, prefix="/api", tags=["vocables"])
app.include_router(
    generate_vocables_router, prefix="/generate", tags=["generate"]
)
