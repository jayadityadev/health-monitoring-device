from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db.mongo_db import *

app = FastAPI()

# Models for validation
class Patient(BaseModel):
    name: str
    dob: str
    age: int
    sex: str
    weight: int
    blood_group: str
    photo: str
    medical_records: list
    appointments: list

class Room(BaseModel):
    temperature: float
    live_footage: str
    emergency_status: bool
    last_updated: str

class Appointment(BaseModel):
    patient_id: str
    date: str
    time: str
    doctor: str
    purpose: str

class Emergency(BaseModel):
    patient_id: str
    emergency_type: str
    timestamp: str

class TabletSchedule(BaseModel):
    patient_id: str
    medication: str
    dosage: str
    time: str

# Routes

# Get room details - Working
@app.get("/rooms/{room_id}")
async def get_room(room_id: str):
    room = await rooms_collection.find_one({"_id": room_id})
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

# Get patient details - Working
@app.get("/patients/{patient_id}")
async def get_patient(patient_id: str):
    patient = await patients_collection.find_one({"_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient["_id"] = str(patient["_id"])
    return patient

# Get appointments for a patient - Working
@app.get("/patients/{patient_id}/appointments")
async def get_patient_appointments(patient_id: str):
    appointments = await appointments_collection.find({"patient_id": patient_id}).to_list(length=100)
    return appointments

# Get emergencies for a patient - Working
@app.get("/patients/{patient_id}/emergencies")
async def get_patient_emergencies(patient_id: str):
    emergencies = await emergencies_collection.find({"patient_id": patient_id}).to_list(length=100)
    return emergencies

# Get tablet schedules for a patient - Working
@app.get("/patients/{patient_id}/tablet_schedules")
async def get_tablet_schedules(patient_id: str):
    tablet_schedules = await tablet_schedules_collection.find({"patient_id": patient_id}).to_list(length=100)
    return tablet_schedules

# Create a new room - Working
@app.post("/rooms")
async def create_room(room: Room):
    result = await rooms_collection.insert_one(room.dict())
    return {"_id": str(result.inserted_id)}

# Create a new patient - Working
@app.post("/patients")
async def create_patient(patient: Patient):
    result = await patients_collection.insert_one(patient.dict())
    return {"_id": str(result.inserted_id)}

# Create a new appointment - Working
@app.post("/appointments")
async def create_appointment(appointment: Appointment):
    result = await appointments_collection.insert_one(appointment.dict())
    return {"_id": str(result.inserted_id)}

# Create a new emergency - Working
@app.post("/emergencies")
async def create_emergency(emergency: Emergency):
    result = await emergencies_collection.insert_one(emergency.dict())
    return {"_id": str(result.inserted_id)}

# Create a new tablet schedule - Working
@app.post("/tablet_schedules")
async def create_tablet_schedule(tablet_schedule: TabletSchedule):
    result = await tablet_schedules_collection.insert_one(tablet_schedule.dict())
    return {"_id": str(result.inserted_id)}
