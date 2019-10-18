import React, { useState } from 'react';

import './Form.css';

const Form = ({ submit }) => {
    const [origin, setOrigin] = useState();
    const [dest, setDest] = useState();
    const [algo, setAlgo] = useState();

    const handleSubmit = e => {
        submit(origin, dest, algo);
        e.preventDefault();
    };

    return (
        <form id="form" onSubmit={handleSubmit}>
            <div className="city-select">
                <label onChange={e => setOrigin(e.target.value)}>
                    <span>Origin</span>
                    <input type="text"></input>
                </label>
                <span>⟶</span>
                <label onChange={e => setDest(e.target.value)}>
                    <span>Destination</span>
                    <input type="text"></input>
                </label>
            </div>

            <div className="algo-select" onChange={e => setAlgo(e.target.value)}>
                <label htmlFor="a">
                    <span>A*</span>
                    <input type="radio" name="algorithm" value="a" />
                </label>

                <label htmlFor="dijkstra">
                    <span>Dijkstra</span>
                    <input type="radio" name="algorithm" value="dijkstra" />
                </label>
            </div>

            <input type="submit" value="Submit" />
        </form>
    );
};

export default Form;
