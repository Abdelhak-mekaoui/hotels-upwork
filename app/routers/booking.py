from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime 
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
)

@router.post("/book")
async def book_room(booking: schemas.BookingModel, db: Session = Depends(get_db)):
    booking = crud.create_booking(db, room_id=booking.room_id, start_date=booking.start_date, end_date=booking.end_date, guest_name=booking.guest_name)
    return {"booking_reference_id": booking.id}

@router.get("/", response_model=List[schemas.BookingModel])
async def get_bookings(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, start_date, end_date)
    return bookings

@router.delete("/cancel")
async def cancel_booking(booking_cancel: schemas.BookingCancelModel, db: Session = Depends(get_db)):
    crud.cancel_booking(db, booking_reference_id=booking_cancel.booking_reference_id)
    return {"detail": "Booking successfully canceled"}
