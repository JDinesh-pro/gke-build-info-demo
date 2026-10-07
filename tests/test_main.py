from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_build_info():
    response = client.get("/build-info")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "build-info-api"
    assert data["version"] == "1.0.0"
    assert data["build_number"] == "local"
    assert data["git_commit"] == "local"
    assert data["environment"] == "development"