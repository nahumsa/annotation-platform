from pydantic import BaseModel


class TextPost(BaseModel):
    """Model for post a text on the api"""

    text: str
