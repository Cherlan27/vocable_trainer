import pytest
from src.services.llm_service.voc_generation import VocGenerator


@pytest.fixture
def voc_generator_mock(mocker):
    return VocGenerator(llm=mocker.MagicMock())


@pytest.fixture
def sample_llm_response():
    return (
        "GPT4 Correct User: Generate a list of French vocables in a Python"
        " array format for the given topic with its English translation.\n"
        "The array should contain 20 vocables related to the topic.\n\n"
        'Example output:\n["pomme - apple", "banane - banana",'
        ' "fromage - cheese", "pain - bread", "lait - milk"]\n\n'
        "The topic is: computer\n "
        "GPT4 Correct Assistant:"
        ' ["ordinateur - computer", "clavier - keyboard",'
        ' "souris - mouse", "écran - screen",'
        ' "ordre - command"]'
    )


def test_extract_vocables_from_response(
    voc_generator_mock, sample_llm_response
):
    expected_vocables = [
        {"word": "ordinateur", "translation": "computer"},
        {"word": "clavier", "translation": "keyboard"},
        {"word": "souris", "translation": "mouse"},
        {"word": "écran", "translation": "screen"},
        {"word": "ordre", "translation": "command"},
    ]

    vocables = voc_generator_mock.extract_vocables_from_response(
        sample_llm_response
    )
    assert vocables == expected_vocables


def test_generate_vocables_for_topic(voc_generator_mock):
    topic = "computer"
    voc_generator_mock.llm.generate.return_value = (
        "GPT4 Correct User: Generate a list of French vocables in a Python"
        " array format for the given topic with its English translation.\n"
        "The array should contain 20 vocables related to the topic.\n\n"
        'Example output:\n["pomme - apple", "banane - banana",'
        ' "fromage - cheese", "pain - bread", "lait - milk"]'
        "\n\nThe topic is: computer\n "
        "GPT4 Correct Assistant:"
        ' ["ordinateur - computer", "clavier - keyboard",'
        ' "souris - mouse", "écran - screen",'
        ' "ordre - command", "ordinateur - computer"]'
    )

    vocables = voc_generator_mock.generate_vocables_for_topic(topic)
    expected_vocables = [
        {"word": "ordinateur", "translation": "computer"},
        {"word": "clavier", "translation": "keyboard"},
        {"word": "souris", "translation": "mouse"},
        {"word": "écran", "translation": "screen"},
        {"word": "ordre", "translation": "command"},
    ]

    assert vocables == expected_vocables
