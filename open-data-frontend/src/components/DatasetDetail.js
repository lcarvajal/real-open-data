import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

export default function DatasetDetail(props) {
  const [dataset, setDataset] = useState({});
  const { id } = useParams();

  useEffect(() => {
    axios.get('http://localhost:8000/datasets/' + id)
      .then(response => {
        console.log(response.data);
        setDataset(response.data.dataset);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      {
        dataset ? (
          <p>{dataset.title}</p>
        ) : (
          <p>Dataset loading</p>
        )
      }
    </div>
  );
}