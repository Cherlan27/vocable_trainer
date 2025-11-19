import os

import yaml


def read_prompt(template_name: str) -> dict:
    """
    Reads a prompt template from the prompts directory.

    Args:
        template_name (str): The name of the prompt template file.

    Returns:
        dict: The loaded prompt template.
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base_path, "prompts", template_name)
    try:
        with open(prompt_path, "r", encoding="utf-8") as file:
            template = yaml.safe_load(file)
        return template
    except Exception as e:
        raise FileNotFoundError(f"Could not read prompt template: {e}")
