import pytest
from collections.abc import Generator


@pytest.fixture(scope="module")
def api_headers() -> Generator:
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer ",
    }
    yield headers
