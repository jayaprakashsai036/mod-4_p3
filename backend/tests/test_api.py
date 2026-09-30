from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat():
    response = client.post(
        "/chat",
        json={
            "session_id": "test-session",
            "message": "Hello"
        }
    )
    assert response.status_code == 200
    assert "reply" in response.json()
    assert "history_length" in response.json()
