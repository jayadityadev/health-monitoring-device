from fastapi import APIRouter, HTTPException
from models.models import Room
from db.mongo_db import rooms_collection

router = APIRouter()

@router.get("/rooms/{room_id}")
async def get_room(room_id: str):
    room = await rooms_collection.find_one({"_id": room_id})
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.post("/rooms")
async def create_room(room: Room):
    result = await rooms_collection.insert_one(room.dict())
    return {"_id": str(result.inserted_id)}