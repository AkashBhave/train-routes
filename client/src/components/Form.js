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
                <label htmlFor="bfs">
                    <span>BFS</span>
                    <input type="radio" name="algorithm" value="bfs" />
                </label>
                <label htmlFor="iddfs">
                    <span>ID-DFS</span>
                    <input type="radio" name="algorithm" value="iddfs" />
                </label>
            </div>

            <button type="submit" value="Submit">
                Visualize
            </button>
        </form>
    );
};

export default Form;
