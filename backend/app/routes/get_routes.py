from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from db.mongo_db import patients_collection

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

@router.get("/patients_data")
async def get_patients_data():
    patients = await patients_collection.find().to_list(length=None)
    patients_data = []
    for patient in patients:
        patient["_id"] = str(patient["_id"])
        patients_data.append(patient)

    return patients_data

@router.get("/")
async def main():
    return {"message": "Hello World"}

app.include_router(router)