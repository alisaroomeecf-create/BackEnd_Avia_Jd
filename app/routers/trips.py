from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.trip import TripCreate
from app.services.trip_service import TripServise
from database import get_db

router=APIRouter(prefix="/trips",tags=["Trips"])