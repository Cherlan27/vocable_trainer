import pytest
from fastapi.testclient import TestClient
from src.api.app import app


@pytest.mark.asyncio
async def test_get_vocables():
    client = TestClient(app, base_url="http://test")
    response = client.get("/api/cards")
    assert response.status_code == 200
    assert response.json() is None
