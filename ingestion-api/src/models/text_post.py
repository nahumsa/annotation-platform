from pydantic import BaseModel


class TextPost(BaseModel):
    text: str
