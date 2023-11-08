import os
from integrations.mastodon import get_mastodon_timeline_text
from model.config import Config


def test_mastodon():
    result = get_mastodon_timeline_text(
        "mentalhealth",
        config=Config(bearer_token=os.environ["BEARER_TOKEN"], url="https://mastodon.social/api", limit=5),
    )
    assert len(result) <= 5
