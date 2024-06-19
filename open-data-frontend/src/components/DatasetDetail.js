import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto'; // Needed for chart.js to function.

export default function DatasetDetail(props) {
  const [responseData, setResponseData] = useState({});
  const { id } = useParams();

  useEffect(() => {
    axios.get('http://localhost:8000/datasets/' + id)
      .then(response => {
        console.log(response.data);
        setResponseData(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      {
        responseData && responseData.dataset ? (
          <>
            <h1>{responseData.dataset.title}</h1>
            <p>
              Showing data for {responseData.chart.filter_title}:
              <select id="filter">
                {responseData.chart.filter_options.map(option =>
                  <option key={option} value={option}>{option}</option>
                )}
              </select>
            </p>
            <div>
              <Line data={responseData.chart_data} options={responseData.chart_options} />
            </div>
          </>
        ) : (
          <p>Dataset loading</p>
        )
      }
    </div >
  );
}