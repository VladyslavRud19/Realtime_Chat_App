class ConnectionMonitor:
    def __init__(self):
        self.stats = {}  # {room_id: connection_count}

    def increment_connection(self, room_id: str):
        self.stats[room_id] = self.stats.get(room_id, 0) + 1
        print(f"Room {room_id}: {self.stats[room_id]} connections")

    def decrement_connection(self, room_id: str):
        if room_id in self.stats:
            self.stats[room_id] -= 1
            if self.stats[room_id] <= 0:
                del self.stats[room_id]
            print(f"Room {room_id}: {self.stats[room_id]} connections")