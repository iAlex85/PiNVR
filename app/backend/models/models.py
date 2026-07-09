from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.backend.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Camera(Base):
    __tablename__ = "cameras"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    stream_url = Column(String)
    enabled = Column(Boolean, default=True)

class Recording(Base):
    __tablename__ = "recordings"
    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(Integer, index=True)
    filepath = Column(String)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    is_motion_event = Column(Boolean, default=False)