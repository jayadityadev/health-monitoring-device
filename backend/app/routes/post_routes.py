from fastapi import APIRouter, HTTPException
from models.models import Patient, Room, Appointment, Emergency, TabletSchedule
from db.mongo_db import patients_collection, rooms_collection, appointments_collection, emergencies_collection, tablet_schedules_collection

router = APIRouter()

@router.post("/patients_data")
async def create_patient_data(data: Patient):
    latest_patient = await patients_collection.find_one(sort=[("_id", -1)])
    if latest_patient and "patient_id" in latest_patient:
        latest_id_num = int(latest_patient["patient_id"].split("_")[1])
        new_patient_id = f"patient_{latest_id_num + 1:03d}"
    else:
        new_patient_id = "patient_001"
    
    data_dict = data.dict()
    data_dict["patient_id"] = new_patient_id
    
    result = await patients_collection.insert_one(data_dict)
    return {"_id": str(result.inserted_id), "patient_id": new_patient_id}

@router.post("/rooms")
async def create_room(room: Room):
    result = await rooms_collection.insert_one(room.dict())
    return {"_id": str(result.inserted_id)}

@router.post("/emergencies")
async def create_emergency(emergency: Emergency):
    result = await emergencies_collection.insert_one(emergency.dict())
    return {"_id": str(result.inserted_id)}