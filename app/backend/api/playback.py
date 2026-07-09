from fastapi import APIRouter

router = APIRouter(prefix="/api/playback", tags=["Playback"])

@router.get("/{camera_id}")
async def get_recordings(camera_id: int):
    return {"camera": camera_id, "recordings": []}