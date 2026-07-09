from fastapi import FastAPI
from app.backend.core.database import engine, Base
from app.backend.api import auth, cameras, playback, storage, ws

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PiNVR")

app.include_router(auth.router)
app.include_router(cameras.router)
app.include_router(playback.router)
app.include_router(storage.router)
app.include_router(ws.router)

@app.get("/")
async def root():
    return {"message": "PiNVR API Online"}