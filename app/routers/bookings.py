from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import BookingCreate
from app.services.booking_service import BookingServise
from database import get_db

router=APIRouter(prefix="/bookings",tags=["Bookings"])

@router.get("/")
async def create_booking(data:BookingCreate,db:AsyncSession=Depends(get_db)):
    return await BookingServise.create_booking(db,data)

@router.get("/")
async def get_booking(db:AsyncSession=Depends(get_db)):
    return await BookingServise.get_all(db)