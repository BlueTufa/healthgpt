from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health_check():
    result = client.get("/")
    assert result.status_code == 200
