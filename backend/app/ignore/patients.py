from fastapi import APIRouter, HTTPException
from models.models import Patient
from db.mongo_db import patients_collection, appointments_collection, emergencies_collection, tablet_schedules_collection

router = APIRouter()

@router.get("/patients/{patient_id}/all_data")
async def get_all_patient_data(patient_id: str):
    patient = await patients_collection.find_one({"_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient["_id"] = str(patient["_id"])
    appointments = await appointments_collection.find({"patient_id": patient_id}).to_list(length=100)
    emergencies = await emergencies_collection.find({"patient_id": patient_id}).to_list(length=100)
    tablet_schedules = await tablet_schedules_collection.find({"patient_id": patient_id}).to_list(length=100)

    return {
        "patient": patient,
        "appointments": appointments,
        "emergencies": emergencies,
        "tablet_schedules": tablet_schedules
    }

@router.get("/patients/{patient_id}")
async def get_patient(patient_id: str):
    patient = await patients_collection.find_one({"_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient["_id"] = str(patient["_id"])
    return patient

@router.get("/patients/{patient_id}/appointments")
async def get_patient_appointments(patient_id: str):
    appointments = await appointments_collection.find({"patient_id": patient_id}).to_list(length=100)
    return appointments

@router.get("/patients/{patient_id}/emergencies")
async def get_patient_emergencies(patient_id: str):
    emergencies = await emergencies_collection.find({"patient_id": patient_id}).to_list(length=100)
    return emergencies

@router.get("/patients/{patient_id}/tablet_schedules")
async def get_tablet_schedules(patient_id: str):
    tablet_schedules = await tablet_schedules_collection.find({"patient_id": patient_id}).to_list(length=100)
    return tablet_schedules

@router.post("/patients")
async def create_patient(patient: Patient):
    result = await patients_collection.insert_one(patient.dict())
    return {"_id": str(result.inserted_id)}