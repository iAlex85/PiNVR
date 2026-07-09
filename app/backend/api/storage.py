from fastapi import APIRouter

router = APIRouter(prefix="/api/storage", tags=["Storage"])

@router.get("/stats")
async def get_storage_stats():
    return {"status": "ok", "usage": "0%"}