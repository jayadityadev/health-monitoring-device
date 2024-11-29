from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb://localhost:27017"
#uri = "mongodb+srv://jayadityadev:<db_password>@cluster0.14qlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(uri)
database = client["health-device"]

# Collections
patients_collection = database["patient_data"]
rooms_collection = database["rooms"]
appointments_collection = database["appointments"]
emergencies_collection = database["emergencies"]
tablet_schedules_collection = database["tablet_schedules"]
