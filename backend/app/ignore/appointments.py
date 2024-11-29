from fastapi import APIRouter
from models.models import Appointment
from db.mongo_db import appointments_collection

router = APIRouter()

@router.post("/appointments")
async def create_appointment(appointment: Appointment):
    result = await appointments_collection.insert_one(appointment.dict())
    return {"_id": str(result.inserted_id)}