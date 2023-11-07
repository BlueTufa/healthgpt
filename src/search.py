from util.common import log
from fastapi import Depends
from fastapi.routing import APIRouter
from model.config import Config, get_config
import requests

# TODO: authorization required.
# jwt_auth = JwtBearerTokenAuthorizer()
router = APIRouter()


@router.get("/search")
async def search(tag: str, config: Config = Depends(get_config)):
    url = f"{config.url}/v1/timelines/tag/{tag}?limit={config.limit}"
    log.debug("Searching mastodon timeline for {tag} using {url}")
    search_results = requests.get(
        url,
        headers={"Authorization": f"Bearer {config.bearer_token}"},
    )
    if search_results.status_code == 200:
        return search_results.content
