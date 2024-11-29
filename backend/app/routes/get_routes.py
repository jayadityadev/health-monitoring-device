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

@router.get("/check_emergency")
async def check_emergency():
    # Fetch all emergencies
    emergencies = await emergencies_collection.find().to_list(length=None)
    # Check if there are any emergencies
    if not emergencies:
        raise HTTPException(status_code=404, detail="No emergencies found")
    # Prepare the final list to store all emergencies' data
    emergencies_data = []
    for emergency in emergencies:
        # Convert ObjectId to string
        emergency["_id"] = str(emergency["_id"])
        # Append the emergency data directly to the list
        emergencies_data.append(emergency)
    return emergencies_data