import React from 'react';

import './Footer.css';

const Footer = () => (
    <footer>
        <p>
            An experiment by <a href="https://akashbhave.com">Akash Bhave</a>
        </p>
        <p>
            <a href="https://github.com/AkashBhave/train-routes/blob/master/LICENSE">LICENSE</a> (MIT)
        </p>
        <div>
            <a href="https://www.github.com/AkashBhave/train-routes">
                <img
                    height="30"
                    width="30"
                    src="https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/github.svg"
                    alt="GitHub"
                />
            </a>
        </div>
    </footer>
);

export default Footer;
