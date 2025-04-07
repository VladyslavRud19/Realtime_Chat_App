import { useState } from 'react';

function FileUploader({ sendMessage }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      sendMessage({
        type: 'file',
        filename: file.name,
        content: event.target.result, // Base64 encoded
      });
    };
    reader.readAsDataURL(file);
    setFile(null);
  };

  return (
    <div className="file-uploader">
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit" disabled={!file}>Upload</button>
      </form>
    </div>
  );
}

export default FileUploader;