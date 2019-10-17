import React, { Component } from 'react';
import { Map, TileLayer } from 'react-leaflet';

export default class M extends Component {
    state = {
        lat: 39.315701,
        lng: -99.636657,
        zoom: 4
    };

    render() {
        const position = [this.state.lat, this.state.lng];
        return (
            <Map center={position} zoom={this.state.zoom}>
                <TileLayer
                    attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
            </Map>
        );
    }
}
