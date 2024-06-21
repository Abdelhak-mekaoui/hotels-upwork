from pydantic import BaseModel, Field
from datetime import datetime

class RoomModel(BaseModel):
    id: int
    name: str
    description: str
    number_of_beds: int
    price: float
    availability: datetime

    class Config:
        from_attributes = True 

class BookingModel(BaseModel):
    room_id: int
    start_date: datetime
    end_date: datetime
    guest_name: str

class BookingCancelModel(BaseModel):
    booking_reference_id: int
