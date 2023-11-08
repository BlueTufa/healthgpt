import os
import pytest
from collections.abc import Generator
from unittest.mock import Mock


@pytest.fixture(scope="module")
def api_headers() -> Generator:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('BEARER_TOKEN', '')}",
    }
    yield headers


@pytest.fixture()
def mock_chatgpt(mocker):
    mocker.patch("openai.OpenAI", return_value=Mock)
