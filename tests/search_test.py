from fastapi.testclient import TestClient
from api import app
from unittest.mock import patch


client = TestClient(app)


def test_search(api_headers):
    with patch("search.send_to_chatgpt", return_value=MockGPT("Magic mock gpt result")) as gpt:
        result = client.get("/timeline/search?tag=mentalhealth", headers=api_headers)
        assert result.status_code == 200
        gpt.assert_called()


class MockGPT:
    def __init__(self, content: str):
        self.content = content
