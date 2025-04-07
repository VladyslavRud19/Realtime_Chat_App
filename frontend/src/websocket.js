import { useEffect, useState } from 'react';

export function useWebSocket(url) {
  const [ws, setWs] = useState(null);
  const [messages, setMessages] = useState([]);
  const [connectionStatus, setConnectionStatus] = useState('disconnected');

  useEffect(() => {
    const websocket = new WebSocket(url);

    websocket.onopen = () => setConnectionStatus('connected');
    websocket.onclose = () => setConnectionStatus('disconnected');
    websocket.onerror = () => setConnectionStatus('error');
    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);
    };

    setWs(websocket);

    return () => websocket.close();
  }, [url]);

  const sendMessage = (message) => {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(message));
    }
  };

  return { messages, sendMessage, connectionStatus };
}