from pydantic import BaseModel


class Timeline(BaseModel):
    title: str
    text: str
