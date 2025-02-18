import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [matchScore, setMatchScore] = useState(null);
  const [suggestions, setSuggestions] = useState([]);

  const handleResumeChange = (e) => {
    setResume(e.target.files[0]);
  };

  const handleJobDescriptionChange = (e) => {
    setJobDescription(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('job_description', jobDescription);

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setMatchScore(response.data.match_score);
      setSuggestions(response.data.suggestions);
    } catch (error) {
      console.error('Error uploading the files', error);
    }
  };

  const handleReset = () => {
    setResume(null);
    setJobDescription('');
    setMatchScore(null);
    setSuggestions([]);
    document.getElementById('resume-input').value = null;
  };

  return (
    <div className="container">
      <h1>Resume Matcher</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" id="resume-input" onChange={handleResumeChange} />
        <textarea
          rows="10"
          placeholder="Paste job description here..."
          value={jobDescription}
          onChange={handleJobDescriptionChange}
        ></textarea>
        <button type="submit">Match</button>
        <button type="button" onClick={handleReset}>Reset</button>
      </form>
      {matchScore !== null && (
        <div>
          <h2>Match Score: {matchScore.toFixed(2)*100}%</h2>
          {suggestions.length > 0 && (
            <div>
              <h3>Suggestions for Improvement:</h3>
              <ul>
                {suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;