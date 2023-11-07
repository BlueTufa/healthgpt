import os
import pytest
from collections.abc import Generator


@pytest.fixture(scope="module")
def api_headers() -> Generator:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('BEARER_TOKEN', '')}",
    }
    yield headers
