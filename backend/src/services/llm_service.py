import json
from typing import Optional

import requests

from backend.src.models.api_models import PromptData


class LLMHandler:
    def __init__(self, url: str):
        self.url = url

    def set_systemprompt(custom_prompt: Optional[str]):
        pass

    def generate(self, data: PromptData) -> str:
        """
        Send prompt data to LLM model and get response

        Args:
            data (PromptData): A prompt string with max tokens.

        Returns:

        """
        try:
            response = requests.post(url=self.url, json=data.model_dump())
            return str(json.loads(response.text).get("response"))
        except Exception as e:
            print(f"Error with API: {e}")
