import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './App.css';

import Map from './components/Map';

const App = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:5000/solve?algorithm=a&city1=Leon&city2=Montreal').then(res => setData(res.data));
    }, []);

    return <div className="App">{data ? <Map points={data.solution} /> : <div>Loading...</div>}</div>;
};

export default App;
