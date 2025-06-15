import React, { useState } from 'react';
import UploadPhoto from './components/UploadPhoto';
import OutfitList from './components/OutfitList';

function App() {
  const [userData, setUserData] = useState(null);
  const [tryOnResult, setTryOnResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-6 font-sans">
      <h1 className="text-3xl font-bold text-center mb-6">Virtual Fashion Stylist</h1>
      <UploadPhoto setUserData={setUserData} />
      {userData && <OutfitList userData={userData} setTryOnResult={setTryOnResult} />}
      {tryOnResult && (
        <div className="mt-6 text-center">
          <h3 className="text-lg font-semibold mb-2">Try-On Result</h3>
          <img src={`http://localhost:5000${tryOnResult}`} alt="Try On Result" className="inline-block border rounded" />
        </div>
      )}
    </div>
  );
}

export default App;
