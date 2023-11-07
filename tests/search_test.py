from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health_check(api_headers):
    result = client.get("/timeline/search?tag=mentalhealth", headers=api_headers)
    assert result.status_code == 200
