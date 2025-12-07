from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from src.api.app import app
from src.services import deps


def test_generate_new_vocables():
    mock = MagicMock()
    mock.generate_vocables_for_topic.return_value = [
        {"word": "test", "translation": "Test"}
    ]

    app.dependency_overrides[deps.get_voc_generator] = lambda: mock

    client = TestClient(app)

    response = client.post(
        "/generate/new_vocables", json={"topic": "test_topic"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "vocables": [{"word": "test", "translation": "Test"}]
    }
