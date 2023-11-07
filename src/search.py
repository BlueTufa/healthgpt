from util.common import log
from fastapi import Depends
from fastapi.routing import APIRouter
from model.config import Config, get_config
from model.timeline import Timeline
import requests

# TODO: authorization required.
# jwt_auth = JwtBearerTokenAuthorizer()
router = APIRouter()


@router.get("/search")
async def search(tag: str, config: Config = Depends(get_config)):
    # Unfortunately, the Twitter API is no longer free.
    # In the interests of managing the scope of this project,
    # I found a somewhat similar but lacking timeline view in the Mastodon API.
    # This returns a result-limited set of Mastodon "statuses" by a particular tag.
    url = f"{config.url}/v1/timelines/tag/{tag}?limit={config.limit}"
    log.debug("Searching mastodon timeline for {tag} using {url}")

    # Architecturally, this type of double-hop REST call is discouraged.
    # This is especially problematic for open-ended operations such as a search.
    # My recommendation would be to build out a better async pattern using
    # a middleware such as Celery, possibly backed by a redis store.
    search_results = requests.get(
        url,
        headers={"Authorization": f"Bearer {config.bearer_token}"},
    )
    if search_results.status_code == 200:
        return search_results.content


def get_mastodon_timeline_text(config: Config) -> Timeline:
    pass
