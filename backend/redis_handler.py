import redis
import json
from fastapi import WebSocket  # Додаємо імпорт WebSocket

class RedisHandler:
    def __init__(self):
        self.redis = None
        self.pubsub = None

    async def connect(self):
        self.redis = await redis.create_redis_pool("redis://redis:6379")
        self.pubsub = self.redis.pubsub()

    async def disconnect(self):
        await self.redis.close()

    async def broadcast_to_room(self, room_id: str, message: dict):
        await self.redis.publish(f"room:{room_id}", json.dumps(message))

    async def listen_to_room(self, room_id: str, websocket: WebSocket):
        await self.pubsub.subscribe(f"room:{room_id}")
        async for message in self.pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"])