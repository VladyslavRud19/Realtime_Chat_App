from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.rooms = {}  # {room_id: [websocket1, websocket2, ...]}

    async def connect(self, websocket: WebSocket, room_id: str, user: str):
        await websocket.accept()
        if room_id not in self.rooms:
            self.rooms[room_id] = []
        self.rooms[room_id].append(websocket)
        await websocket.send_json({"type": "system", "message": f"Welcome, {user}!"})

    def disconnect(self, websocket: WebSocket, room_id: str):
        if room_id in self.rooms and websocket in self.rooms[room_id]:
            self.rooms[room_id].remove(websocket)
            if not self.rooms[room_id]:
                del self.rooms[room_id]