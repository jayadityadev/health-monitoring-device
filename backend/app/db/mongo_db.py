from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
database = client["health-device"]

# Collections
patients_collection = database["patient_data"]
rooms_collection = database["rooms"]
appointments_collection = database["appointments"]
emergencies_collection = database["emergencies"]
tablet_schedules_collection = database["tablet_schedules"]
