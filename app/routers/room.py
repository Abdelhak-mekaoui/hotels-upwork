from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app import crud, models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
)

@router.get("/available", response_model=List[schemas.RoomModel])
async def search_available_rooms(start_date: datetime, end_date: datetime, beds: int = 0, db: Session = Depends(get_db)):
    rooms = crud.get_available_rooms(db, start_date, end_date, beds)
    return rooms
