import React from 'react';
import axios from 'axios';

function OutfitList({ userData, setTryOnResult }) {
  const handleTryOn = async (outfitImage) => {
    try {
      const res = await axios.post('http://localhost:5000/tryon', {
        image_path: userData.image_path,
        outfit_id: outfitImage
      });
      setTryOnResult(res.data.result_image);
    } catch (error) {
      alert('Try-On failed: ' + error.message);
    }
  };

  return (
    <div className="mt-8">
      <h2 className="text-xl font-semibold mb-2">User Profile</h2>
      <p><strong>Age:</strong> {userData.age}</p>
      <p><strong>Gender:</strong> {userData.gender}</p>
      <p><strong>Measurements:</strong></p>
      <ul className="ml-4 list-disc">
        {Object.entries(userData.measurements).map(([key, value]) => (
          <li key={key}>{key.replace('_', ' ')}: {value} cm</li>
        ))}
      </ul>

      <h2 className="text-xl font-semibold mt-6 mb-2">Recommended Outfits</h2>
      <div className="grid grid-cols-2 gap-4">
        {userData.outfits.map((outfit) => (
          <div key={outfit.id} className="p-4 bg-white rounded shadow">
            <img src={`http://localhost:5000/static/outfits/${outfit.image}`} alt={outfit.name} className="w-full h-40 object-cover rounded" />
            <p className="mt-2 font-medium">{outfit.name}</p>
            <button
              className="bg-green-500 text-white px-3 py-1 mt-2 rounded hover:bg-green-600"
              onClick={() => handleTryOn(outfit.image)}
            >
              Try On
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default OutfitList;
