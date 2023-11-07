import os
from pydantic import BaseModel, Field


class Config(BaseModel):
    bearer_token: str
    url: str
    limit: int = Field(ge=5, le=7, description="The requirements state that the limit should be between 5 and 7 items")


def get_config() -> Config:
    return Config(
        bearer_token=os.environ.get("BEARER_TOKEN", ""),
        url=os.environ.get("BASE_URL", "https://mastodon.social/api"),
        limit=int(os.environ.get("DEFAULT_LIMIT", 5)),
    )
