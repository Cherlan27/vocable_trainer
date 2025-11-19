from langchain_core.prompts import PromptTemplate
from src.models.api_models import ChatMessage, PromptData
from src.services.llm_service.llm_handler import LLMHandler
from src.services.llm_service.utils.prompt_reader import read_prompt
from src.services.llm_service.utils.voc_parser import parse_str_to_vocables


class VocGenerator:
    def __init__(self, llm: LLMHandler):
        self.llm = llm

    def generate_vocables_for_topic(self, topic: str) -> list[dict]:
        """
        Generate vocables for a given topic using the LLM service.

        Args:
            topic (str): The topic for which to generate vocables.

        Returns:
            str: The generated vocables.

        """

        template = read_prompt("voc_generation.yaml")

        prompt = PromptTemplate(
            input_variables=["topic"],
            template=template["prompts"][0]["template"],
        )

        response = self.llm.generate(
            PromptData(
                messages=[
                    ChatMessage(
                        role="user", content=prompt.format(topic=topic)
                    )
                ],
                max_new_tokens=1000,
            )
        )

        voc_list = self.extract_vocables_from_response(response)
        unqiue_vocables = {v["word"]: v for v in voc_list}

        return [v for v in unqiue_vocables.values()]

    def extract_vocables_from_response(self, response: str) -> list[dict]:
        """
        Extract vocables from the LLM response.

        Args:
            response (str): The response from the LLM.

        Returns:
            list[dict]: A list of vocables extracted from the response.
        """
        output = response.split("GPT4 Correct Assistant:")[1].strip()
        try:
            parsed_vocables = parse_str_to_vocables(output)
        except ValueError:
            Exception("Could not parse vocables from LLM response.")
        return parsed_vocables
