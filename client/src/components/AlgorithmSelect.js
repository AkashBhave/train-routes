import React from 'react';

import './AlgorithmSelect.css';

const AlgorithmSelect = () => {
    return (
        <div className="algo-select">
            <input type="radio" name="algorithm" value="A*" />
            <label for="A*">A*</label>
            <input type="radio" name="algorithm" value="Dijkstra" />
            <label for="Dijkstra">Dijkstra</label>
        </div>
    );
};

export default AlgorithmSelect;
