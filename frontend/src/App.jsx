import { useState } from 'react';
import ChatRoom from './components/ChatRoom';
import FileUploader from './components/FileUploader';
import ConnectionStatus from './components/ConnectionStatus';
import { useWebSocket } from './websocket';

function App() {
  const [roomId, setRoomId] = useState('general');
  const [token, setToken] = useState('your-jwt-token'); // Отримати з авторизації

  const { messages, sendMessage, connectionStatus } = useWebSocket(
    `ws://localhost:8000/ws/${roomId}/${token}`
  );

  return (
    <div className="app">
      <h1>Real-Time Chat</h1>
      <ConnectionStatus status={connectionStatus} />
      <input
        value={roomId}
        onChange={(e) => setRoomId(e.target.value)}
        placeholder="Room ID"
      />
      <ChatRoom messages={messages} sendMessage={sendMessage} />
      <FileUploader sendMessage={sendMessage} />
    </div>
  );
}

export default App;