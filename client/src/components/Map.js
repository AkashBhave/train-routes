import React, { useRef, useState, useEffect } from 'react';
import { Map, TileLayer, Polyline } from 'react-leaflet';

import './Map.css';

// "Custom" callback to allow `setInterval` with state
// Adapted from https://overreacted.io/making-setinterval-declarative-with-react-hooks/
const useInterval = (callback, delay) => {
    const savedCallback = useRef();

    // Remember the latest callback.
    useEffect(() => {
        savedCallback.current = callback;
    }, [callback]);

    // Set up the interval.
    useEffect(() => {
        function tick() {
            savedCallback.current();
        }
        if (delay !== null) {
            let id = setInterval(tick, delay);
            return () => clearInterval(id);
        }
    }, [delay]);
};

const M = props => {
    const [lat, setLat] = useState(39.315701);
    const [lon, setLon] = useState(-99.636657);
    const [zoom, setZoom] = useState(4);

    const [pointsI, setPointsI] = useState(0);

    // Keep updating the end index while index is below the total length
    useInterval(
        () => {
            if (props.active) {
                setPointsI(pointsI + 100);
            }
        },
        props.data ? (pointsI < props.data.solution.length ? 10 : null) : null
    );

    return (
        <>
            <div id="above-map">
                <div id="controls">
                    <button onClick={() => props.setActive(true)}>Play</button>
                    <button onClick={() => props.setActive(false)}>Pause</button>
                    <button
                        onClick={() => {
                            props.setActive(false);
                            setPointsI(0);
                        }}>
                        Reset
                    </button>
                </div>
                {props.data ? <div id="info">Completed in {Number(props.data.runtime.toFixed(6))} sec.</div> : null}
            </div>
            <Map center={[lat, lon]} zoom={zoom} id="map">
                <TileLayer
                    attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {props.data
                    ? props.data.solution
                          .slice(0, pointsI)
                          .map((point, i) => <Polyline weight="1" key={i} color="red" positions={point} />)
                    : null}
            </Map>
        </>
    );
};

export default M;
