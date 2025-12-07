from src.services.llm_service.utils.prompt_reader import read_prompt


def test_read_prompt_success():
    template = read_prompt("voc_generation.yaml")
    assert "prompts" in template
    assert isinstance(template["prompts"], list)
    assert "template" in template["prompts"][0]


def test_read_prompt_file_not_found():
    try:
        read_prompt("non_existent_file.yaml")
    except FileNotFoundError as e:
        assert "Could not read prompt template" in str(e)
