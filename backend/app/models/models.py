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
    appointment_id: str
    appointment_date: str
    appointment_time: str
    appointment_doctor: str
    appointment_purpose: str
    appointment_status: str
    tab_sch_id: str
    medications: list
    alert_status: bool
    alert_timestamp: str
    alert_resolved: bool

class Room(BaseModel):
    temperature: float
    live_footage: str
    emergency_status: bool
    last_updated: str

class TabletSchedule(BaseModel):
    patient_id: str
    medication: str
    dosage: str
    time: str