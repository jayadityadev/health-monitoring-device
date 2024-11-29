from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    dob: str
    age: int
    sex: str
    weight: int
    blood_group: str
    photo: str
    medical_records: list
    appt_id: str
    appt_date: str
    appt_time: str
    appt_doctor: str
    appt_purpose: str
    appt_status: str
    tab_sch_id: str
    medications: list

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