from fastapi import APIRouter
from models.models import TabletSchedule
from db.mongo_db import tablet_schedules_collection

router = APIRouter()

@router.post("/tablet_schedules")
async def create_tablet_schedule(tablet_schedule: TabletSchedule):
    result = await tablet_schedules_collection.insert_one(tablet_schedule.dict())
    return {"_id": str(result.inserted_id)}