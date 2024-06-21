from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_book_room():
    booking_data = {
        "room_id": 1,
        "start_date": "2023-10-01T00:00:00",
        "end_date": "2023-10-07T00:00:00",
        "guest_name": "John Doe"
    }
    response = client.post("/bookings/book", json=booking_data)
    assert response.status_code == 200
    assert "booking_reference_id" in response.json()

def test_get_bookings():
    response = client.get("/bookings?start_date=2023-10-01T00:00:00&end_date=2023-10-07T00:00:00")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cancel_booking():
    booking_cancel_data = {
        "booking_reference_id": 1
    }
    response = client.delete("/bookings/cancel", json=booking_cancel_data)
    assert response.status_code == 200
    assert response.json() == {"detail": "Booking successfully canceled"}
