from fastapi import APIRouter, WebSocket

router = APIRouter(tags=["WebSockets"])

@router.websocket("/ws/system-stats")
async def websocket_stats(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"cpu": 0, "temp": 45})