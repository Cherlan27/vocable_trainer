import uvicorn
from src.api.app import app
from src.logging_config import logger

if __name__ == "__main__":
    logger.info("Starting the backend server...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
