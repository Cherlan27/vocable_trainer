import random
from pathlib import Path

import pandas as pd

from backend.src.config import DATA_PATH


class VocExtracter:
    def __init__(self):
        self.path = Path(DATA_PATH)

    def extract_one_word(
        self,
        word_type: str,
        number: int = -1,
    ) -> pd.DataFrame:
        """
        Extract one random word from the csv file of the given type.

        Args:
            word_type (str): The type of word to extract
            (e.g., "noun", "verb").
            number (int, optional): The index of the word to extract. If -1,
            a random word is chosen. Defaults to -1.

        Returns:
            dict: A dictionary containing the 'form' and 'tags'
            of the extracted word.
        """

        path_to_words = self.path / f"{word_type}.csv"
        french_df = pd.read_csv(path_to_words)
        if number == -1:
            number = int(random.uniform(0, french_df.shape[0]))
        expression = french_df.iloc[number]
        tags = (
            expression["tags"] if isinstance(expression["tags"], str) else []
        )
        output = {
            "form": expression["form"],
            "tags": tags,
        }

        return output
