import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function Datasets() {
    const [datasets, setDatasets] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/datasets/')
            .then(response => {
                setDatasets(response.data);
            })
            .catch(error => {
                console.log(error);
            });
    }, []);

    return (
        <ul>
            {datasets ? (
                datasets.map(dataset => (
                    <li key={dataset.id}>
                        <a>{dataset.title}</a>
                    </li>
                ))
            ) : (
                <p>Loading datasets...</p>
            )}
        </ul>
    );
}