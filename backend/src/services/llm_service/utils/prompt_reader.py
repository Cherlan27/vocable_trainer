import os

import yaml
from langchain_core.prompts import PromptTemplate


def read_prompt(template_name: str, *args) -> str:
    """
    Reads a prompt template from the prompts directory.

    Args:
        template_name (str): The name of the prompt template file.
        *args: Additional arguments to format the prompt template.

    Returns:
        str: The content of the prompt template.
    """

    prompt_path = os.path
    with open(prompt_path, "r", encoding="utf-8") as file:
        template = yaml.safe_load(file)

    prompt = PromptTemplate(input_variables=["topic"], template=template)

    return prompt
