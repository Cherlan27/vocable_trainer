import pytest
from src.models.api_models import ChatMessage, PromptData
from src.services.llm_service.llm_handler import LLMHandler


@pytest.fixture
def llm_handler() -> LLMHandler:
    return LLMHandler(url="http://test-llm-endpoint.com")


def test_generate_success(llm_handler: LLMHandler, mocker):
    mocker_response = mocker.patch("requests.post")
    mocker_response.return_value.text = '{"response": "Test LLM response"}'

    test_data = PromptData(
        messages=[ChatMessage(role="Assistant", content="Test prompt")],
        max_tokens=50,
    )
    test_result = llm_handler.generate(test_data)

    assert test_result == "Test LLM response"


def test_generate_api_failure(llm_handler: LLMHandler, mocker):
    mocker_response = mocker.patch("requests.post")
    mocker_response.side_effect = Exception("API failure")

    test_data = PromptData(
        messages=[ChatMessage(role="Assistant", content="Test prompt")],
        max_tokens=50,
    )
    test_result = llm_handler.generate(test_data)

    assert test_result is None


def test_set_systemprompt(llm_handler: LLMHandler):
    # Placeholder for future implementation
    llm_handler.set_systemprompt("New system prompt")
    assert True
