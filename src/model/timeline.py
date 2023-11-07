from pydantic import BaseModel


class Timeline(BaseModel):
    text: str
    account: str
