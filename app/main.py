from fastapi import FastAPI
from app.routers import room, booking
from app.database import engine, database

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(room.router)
app.include_router(booking.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Run the app with: uvicorn app.main:app --reload
