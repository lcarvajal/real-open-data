import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TestReact() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/datasets/react/')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Hello, World!</h1>
      <p>{message}</p>
    </div>
  );
}

export default TestReact;