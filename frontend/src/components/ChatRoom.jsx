import { useState } from 'react';

function ChatRoom({ messages, sendMessage }) {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    sendMessage({ type: 'text', message: input });
    setInput('');
  };

  return (
    <div className="chat-room">
      <div className="messages">
        {messages.map((msg, idx) => (
          <div key={idx}>
            {msg.type === 'text' ? (
              <p>{msg.user}: {msg.message}</p>
            ) : msg.type === 'file' ? (
              <p>{msg.user} uploaded: <a href={msg.content}>{msg.filename}</a></p>
            ) : (
              <p>{msg.message}</p>
            )}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message"
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default ChatRoom;