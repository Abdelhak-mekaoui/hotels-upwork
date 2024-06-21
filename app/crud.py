from sqlalchemy.orm import Session
from app.models import Room, Booking
from datetime import datetime

def get_available_rooms(db: Session, start_date: datetime, end_date: datetime, beds: int = 0):
    return db.query(Room).filter(Room.availability.between(start_date, end_date)).filter(Room.number_of_beds >= beds).all()

def create_booking(db: Session, room_id: int, start_date: datetime, end_date: datetime, guest_name: str):
    db_booking = Booking(room_id=room_id, start_date=start_date, end_date=end_date, guest_name=guest_name)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings(db: Session, start_date: datetime, end_date: datetime):
    return db.query(Booking).filter(Booking.start_date.between(start_date, end_date)).all()

def cancel_booking(db: Session, booking_reference_id: int):
    db.query(Booking).filter(Booking.id == booking_reference_id).delete()
    db.commit()
