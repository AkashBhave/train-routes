import React, { useRef, useState, useEffect } from 'react';
import { Map, TileLayer, Polyline } from 'react-leaflet';

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

const M = ({ points }) => {
    const [lat, setLat] = useState(39.315701);
    const [lon, setLon] = useState(-99.636657);
    const [zoom, setZoom] = useState(4);

    const [pointsI, setPointsI] = useState(0);

    // Keep updating the end index while index is below the total length
    useInterval(
        () => {
            setPointsI(pointsI + 100);
        },
        pointsI < points.length ? 1 : null
    );

    return (
        <>
            <Map center={[lat, lon]} zoom={zoom}>
                <TileLayer
                    attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {points.slice(0, pointsI).map((point, i) => (
                    <Polyline key={i} color="red" positions={point} />
                ))}
            </Map>
        </>
    );
};

export default M;
