from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_search_available_rooms():
    response = client.get("/rooms/available?start_date=2023-10-01&end_date=2023-10-07&beds=2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
