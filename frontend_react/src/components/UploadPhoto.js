import React, { useState } from 'react';
import axios from 'axios';

function UploadPhoto({ setUserData }) {
  const [image, setImage] = useState(null);

  const handleFileChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('image', image);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData);
      setUserData(response.data);
    } catch (error) {
      alert('Upload failed: ' + (error.response?.data?.error || error.message));
    }
  };

  return (
    <div className="flex flex-col items-center">
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 mt-4 rounded hover:bg-blue-600"
      >
        Upload & Analyze
      </button>
    </div>
  );
}

export default UploadPhoto;
