from typing import Union, Optional

from pydantic import BaseModel

class Word(BaseModel):
    french: str
    tag: Union[list, Optional[str]]