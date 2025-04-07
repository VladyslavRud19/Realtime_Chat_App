function ConnectionStatus({ status }) {
    const statusStyles = {
      connected: { color: 'green' },
      disconnected: { color: 'red' },
      error: { color: 'orange' },
    };
  
    return (
      <div className="connection-status">
        <span style={statusStyles[status] || {}}>
          Connection: {status}
        </span>
      </div>
    );
  }
  
  export default ConnectionStatus;