import React from 'react';
import axios from 'axios';

function RandomDataButton({ setLayout }) {
  const handleGenerateRandomData = async () => {
    try {
      const response = await axios.get('/api/reports/random');
      setLayout(response.data);
    } catch (error) {
      console.error('Error generating random data', error);
    }
  };

  return <button onClick={handleGenerateRandomData}>Generate Random Data</button>;
}

export default RandomDataButton;
