from typing import Any
from pydantic import BaseModel


class DatasetReturn(BaseModel):
    toxic_texts: list[str]
    non_toxic_texts: list[str]
    metadata: dict[str, Any]