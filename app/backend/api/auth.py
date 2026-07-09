from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.backend.core.database import get_db
from app.backend.models.models import User

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
async def login():
    return {"message": "Login endpoint placeholder"}