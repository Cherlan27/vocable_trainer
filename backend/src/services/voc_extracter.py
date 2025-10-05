from pathlib import Path

import pandas as pd

from backend.src.config import DATA_PATH


class VocExtracter:
    def __init__(self):
        self.path = Path(DATA_PATH)

    def extract(self, word_type: str) -> pd.DataFrame:

        path_to_words = self.path / f"{word_type}.csv"
        french_df = pd.read_csv(path_to_words)
        return french_df
        
