import requests
import json
from typing import List
from util.common import log
from model.config import Config
from model.timeline import Timeline


def get_mastodon_timeline_text(tag: str, config: Config) -> List[Timeline]:
    # Unfortunately, the Twitter API is no longer free.
    # In the interests of cutting scope for this project,
    # I found a somewhat similar - but lacking - timeline view in the Mastodon API.
    # This returns a result-limited set of Mastodon "statuses" by a particular tag.
    url = f"{config.url}/v1/timelines/tag/{tag}?limit={config.limit}"
    log.debug("Searching mastodon timeline for {tag} using {url}")

    # Architecturally, this type of double-hop REST call is discouraged.
    # This is especially problematic for open-ended operations such as a search.
    # My recommendation would be to build out a better async pattern using
    # a middleware such as Celery, possibly backed by a redis store.
    # TODO: need an an accept header here.
    search_results = requests.get(
        url,
        headers={"Authorization": f"Bearer {config.bearer_token}"},
    )
    log.debug(search_results)
    if search_results.status_code == 200:
        return list(map(lambda s: mastodon_status_to_timeline(s), json.loads(search_results.text)))

    return []


def mastodon_status_to_timeline(status: dict) -> Timeline:
    if "card" in status and status["card"] is not None:
        return Timeline(title=status["card"]["title"], text=status["card"]["description"])

    if "content" in status and status["content"] is not None:
        return Timeline(title=status["content"], text="")

    return None
