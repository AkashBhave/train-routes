import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './App.css';
import Map from './components/Map';
import Header from './components/Header';
import CitySelect from './components/CitySelect';
import AlgorithmSelect from './components/AlgorithmSelect';

const App = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:5000/solve?algorithm=a&city1=Leon&city2=Montreal').then(res => setData(res.data));
    }, []);

    return (
        <div className="App">
            <div style={{ marginBottom: '30px' }}>
                <Header />
            </div>
            <div style={{ marginBottom: '20px' }}>
                <CitySelect />
            </div>
            <div style={{ marginBottom: '30px' }}>
                <AlgorithmSelect />
            </div>
            <div>{data ? <Map points={data.solution} /> : <div>Loading...</div>}</div>
        </div>
    );
};

export default App;
