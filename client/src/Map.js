import React, { useState } from 'react';
import { Map as M, TileLayer, Marker, Popup } from '../../src';

const Map = () => {
    const lat = useState(51.505);
    const lon = useState(-0.09);
    const zoom = useState(13);

    return (
        <M center={[lat, lon]} zoom={this.state.zoom}>
            <TileLayer
                attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={[lat, lon]}>
                <Popup>
                    A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
            </Marker>
        </M>
    );
};

export default Map;
