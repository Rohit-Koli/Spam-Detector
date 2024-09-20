import React from 'react'
import { useState } from 'react'
import axios from 'axios'
const SpamPredictor = () => {
    const [inputText, setInputText] = useState('');
    const [prediction, setPrediction] = useState('');
  
    const handleSubmit = async () => {
      try {
        const response = await axios.post('http://localhost:5000/predict', {
          text: inputText
        });
        setPrediction(response.data.prediction);
      } catch (error) {
        console.error('Error predicting:', error);
      }
    };
  
    return (
      <div>
        <h1>Spam Detector</h1>
        <textarea 
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <button onClick={handleSubmit}>Check Spam</button>
        {prediction && <p>Prediction: {prediction}</p>}
      </div>
    );
  }
export default SpamPredictor
