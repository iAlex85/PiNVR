from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.backend.core.database import get_db
from app.backend.models.models import Camera

router = APIRouter(prefix="/api/cameras", tags=["Cameras"])

@router.get("/")
async def list_cameras(db: Session = Depends(get_db)):
    return db.query(Camera).all()