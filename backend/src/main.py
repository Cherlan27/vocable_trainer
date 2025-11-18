import uvicorn
from src.api.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
