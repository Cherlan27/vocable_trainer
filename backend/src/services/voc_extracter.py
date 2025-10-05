import random
from pathlib import Path

import pandas as pd

from backend.src.config import DATA_PATH


class VocExtracter:
    def __init__(self):
        self.path = Path(DATA_PATH)

    def extract_one_word(self, word_type: str, number: int = -1) -> pd.DataFrame:
        """
        Extract one random word from the csv file of the given type.

        Args:
            word_type (str): The type of word to extract (e.g., "noun", "verb").
            number (int, optional): The index of the word to extract. If -1, a random word is chosen. Defaults to -1.

        Returns:
            dict: A dictionary containing the 'form' and 'tags' of the extracted word.
        """
        if number == -1:
            number = int(random.Uniform(0, self.extract(word_type).shape[0]))
        path_to_words = self.path / f"{word_type}.csv"
        french_df = pd.read_csv(path_to_words)
        expression = french_df.iloc[number]
        output = {
            "form": expression["form"],
            "tags": expression["tags"] if isinstance(expression["tags"], str) else []
        }
        
        return output
