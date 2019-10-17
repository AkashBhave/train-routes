import React from 'react';

import './Header.css';

const Header = () => (
    <header>
        <h1 className="header-title">
            Train
            <span role="img" aria-label="Train">
                🚆
            </span>
            Routes
        </h1>
        <p>Visualize train routes across the country!</p>
    </header>
);

export default Header;
