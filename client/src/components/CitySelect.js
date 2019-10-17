import React from 'react';

import './CitySelect.css';

const CitySelect = () => {
    return (
        <div className="city-select">
            <div className="city-field">
                <span>Origin</span>
                <input type="text"></input>
            </div>
            <span>⟶</span>
            <div className="city-field">
                <span>Destination</span>
                <input type="text"></input>
            </div>
        </div>
    );
};

export default CitySelect;
