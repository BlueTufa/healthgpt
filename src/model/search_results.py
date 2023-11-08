from pydantic import BaseModel
from model.timeline import Timeline


class SearchResults(BaseModel):
    timeline: Timeline
    message: str
