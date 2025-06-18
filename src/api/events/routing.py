from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter()


# /api/events
@router.get("/")
async def get_events():
    return { "items": "1, 2, 3" }



# /api/events/{event_id}
@router.get("/{event_id}")
async def get_event(event_id: int):
    return { "event_id": event_id }