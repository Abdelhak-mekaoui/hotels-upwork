from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    number_of_beds = Column(Integer)
    price = Column(Float)
    availability = Column(DateTime)

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship("Room")
    start_date = Column(Date)
    end_date = Column(Date)
    guest_name = Column(String)
