from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from model.config import Config, get_config
from model.timeline import Timeline
from model.search_results import SearchResults
from integrations.mastodon import get_mastodon_timeline_text
from integrations.openai import send_to_chatgpt

# TODO: authorization required.
# jwt_auth = JwtBearerTokenAuthorizer()
# router = APIRouter(dependencies=[Depends(jwt_auth)])
router = APIRouter()


@router.get("/search")
async def search(tag: str, config: Config = Depends(get_config)) -> List[SearchResults]:
    # This is a proof-of-concept ONLY and it needs a redesign.
    # This would be way too slow for general consumption.
    # Redis / Celery might be a great fit and I would love to talk about architectural solutions.
    timeline = get_mastodon_timeline_text(tag, config)
    return list(map(lambda t: gpt_response_content(t, send_to_chatgpt(t)), timeline))


def gpt_response_content(timeline: Timeline, gpt_response) -> SearchResults:
    return SearchResults(timeline=timeline, message=gpt_response.content)
