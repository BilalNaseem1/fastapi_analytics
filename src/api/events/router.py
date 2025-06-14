from fastapi import APIRouter

router = APIRouter()


@router.get("/events")
async def get_events():
    return {
        "items": "1, 2, 3"
    }