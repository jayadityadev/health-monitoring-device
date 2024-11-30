from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.mongo_db import patients_collection, emergencies_collection

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4444/"],  # Allow the specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

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

app.include_router(router)