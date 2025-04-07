from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from connection_manager import ConnectionManager
from redis_handler import RedisHandler
from auth import verify_token
from monitoring import ConnectionMonitor
import asyncio
import json

app = FastAPI()
manager = ConnectionManager()
redis = RedisHandler()
monitor = ConnectionMonitor()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.on_event("startup")
async def startup():
    await redis.connect()
    app.state.redis = redis
    app.state.monitor = monitor

@app.on_event("shutdown")
async def shutdown():
    await redis.disconnect()

@app.websocket("/ws/{room_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, token: str):
    user = verify_token(token)
    if not user:
        await websocket.close(code=1008)
        return

    await manager.connect(websocket, room_id, user)
    monitor.increment_connection(room_id)

    pubsub_task = asyncio.create_task(redis.listen_to_room(room_id, websocket))

    try:
        while True:
            data = await websocket.receive_json()
            message_type = data.get("type")

            if message_type == "text":
                await redis.broadcast_to_room(room_id, {
                    "type": "text",
                    "user": user,
                    "message": data["message"]
                })
            elif message_type == "file":
                await redis.broadcast_to_room(room_id, {
                    "type": "file",
                    "user": user,
                    "filename": data["filename"],
                    "content": data["content"]
                })

    except Exception as e:
        pubsub_task.cancel()
        manager.disconnect(websocket, room_id)
        monitor.decrement_connection(room_id)
        await redis.broadcast_to_room(room_id, {
            "type": "system",
            "message": f"{user} disconnected"
        })