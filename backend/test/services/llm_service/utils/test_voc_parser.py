import pytest
from src.services.llm_service.utils.voc_parser import parse_str_to_vocables


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        (
            "[ 'hello' - 'hola', 'goodbye' - 'adiós' ]",
            [
                {"word": "hello", "translation": "hola"},
                {"word": "goodbye", "translation": "adiós"},
            ],
        ),
        (
            '[ "cat" - "gato", "dog" - "perro" ]',
            [
                {"word": "cat", "translation": "gato"},
                {"word": "dog", "translation": "perro"},
            ],
        ),
        (
            "[ 'apple' - 'manzana' ], [ 'banana' - 'plátano' ]",
            [
                {"word": "apple", "translation": "manzana"},
                {"word": "banana", "translation": "plátano"},
            ],
        ),
    ],
)
def test_parse_str_to_vocables(input_str, expected_output):
    parsed_output = parse_str_to_vocables(input_str)
    assert parsed_output == expected_output
