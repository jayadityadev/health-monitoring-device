from fastapi import APIRouter, HTTPException
from db.mongo_db import patients_collection, emergencies_collection

router = APIRouter()

@router.get("/patients_data")
async def get_patients_data():
    # Fetch all patients
    patients = await patients_collection.find().to_list(length=None)

    # Prepare the final list to store all patients' data
    patients_data = []

    for patient in patients:
        # Convert ObjectId to string
        patient["_id"] = str(patient["_id"])

        # Append the patient data directly to the list
        patients_data.append(patient)

    return patients_data