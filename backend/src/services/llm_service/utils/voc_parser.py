import re


def parse_str_to_vocables(response: str) -> list[dict]:
    """
    Parse a string response into a list of vocables.

    Args:
        response (str): The string response containing vocables.

    Returns:
        list[dict]: A list of vocables with 'word' and 'translation' keys.
    """
    vocables = []
    try:
        vocable_entries = re.findall(r"\[(.*?)\]", response)
        for entry in vocable_entries:
            pairs = entry.split(",")
            for pair in pairs:
                word, translation = pair.split(" - ")
                vocables.append(
                    {
                        "word": word.strip().replace("'", "").replace('"', ""),
                        "translation": translation.strip()
                        .replace("'", "")
                        .replace('"', ""),
                    }
                )
    except Exception as e:
        raise ValueError("Could not parse vocables from response.") from e

    return vocables
