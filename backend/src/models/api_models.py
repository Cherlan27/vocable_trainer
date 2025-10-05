from typing import Optional, Union

from pydantic import BaseModel


class Word(BaseModel):
    french: str
    tag: Union[list, Optional[str]]
