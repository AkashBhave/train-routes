import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './App.css';
import Map from './components/Map';
import Header from './components/Header';
import Form from './components/Form';

const App = () => {
    const [data, setData] = useState(null);
    const [mapActive, setMapActive] = useState(false);

    const handleSubmit = (origin, dest, algo) => {
        axios
            .get(`http://localhost:5000/solve?algorithm=${algo}&city1=${origin}&city2=${dest}`)
            .then(res => setData(res.data))
            .catch(err => {
                alert(err);
            });
        setMapActive(true);
    };

    const updateMapActive = state => {
        setMapActive(state);
        console.log('map is', state);
    };

    return (
        <div className="App">
            <div style={{ marginBottom: '30px' }}>
                <Header />
            </div>
            <div style={{ marginBottom: '20px' }}>
                <Form submit={handleSubmit} />
            </div>
            <div>
                <Map active={mapActive} setActive={updateMapActive} data={data || null} />
            </div>
        </div>
    );
};

export default App;
