from fastapi import APIRouter
from models.models import Emergency
from db.mongo_db import emergencies_collection

router = APIRouter()

@router.post("/emergencies")
async def create_emergency(emergency: Emergency):
    result = await emergencies_collection.insert_one(emergency.dict())
    return {"_id": str(result.inserted_id)}