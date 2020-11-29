import React from 'react';
import ReactDOM from 'react-dom';
import mapboxgl from 'mapbox-gl';
import TextField from '@material-ui/core/TextField';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import FormLabel from '@material-ui/core/FormLabel';

mapboxgl.accessToken = 'pk.eyJ1IjoiZGhydXZrZXlhbCIsImEiOiJja2htbmE2NGEwN3YzMzBsZ2I0dWhhZjVhIn0.1QeYm6Ykbj4YH_kcvmLmCg';

class Application extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            lng: -72.5236,
            lat: 42.3795,
            zoom: 13.04
        };
    }

    componentDidMount() {
        const map = new mapboxgl.Map({
            container: this.mapContainer,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [this.state.lng, this.state.lat],
            zoom: this.state.zoom
        });

        map.on('move', () => {
            this.setState({
                lng: map.getCenter().lng.toFixed(4),
                lat: map.getCenter().lat.toFixed(4),
                zoom: map.getZoom().toFixed(2)
            });
        });
    }

    render() {
        return (
            <div className="overall">
                <div className='sidebarStyle'>
                    <div>Longitude: {this.state.lng} | Latitude: {this.state.lat} | Zoom: {this.state.zoom}</div>
                </div>
                <div className='searchStyle'>
                    <TextField
                        color="white"
                        label="Start location"
                        margin="dense"
                        variant="outlined"
                    />
                </div>
                <div className='searchStyle'>
                    <TextField
                        color="white"
                        label="End location"
                        margin="dense"
                        variant="outlined"
                    />
                </div>
                <div className='searchStyle'>
                    <FormControl component="fieldset">
                        <FormLabel component="legend" style={{color: "black", fontWeight: 30}}>Elevation</FormLabel>
                        <RadioGroup>
                            <FormControlLabel value="minimize" control={<Radio />} label="Minimize Elevation" />
                            <FormControlLabel value="maximize" control={<Radio />} label="Maximize Elevation" />
                        </RadioGroup>
                    </FormControl> 
                </div>
                <div ref={el => this.mapContainer = el} className='mapContainer' />
            </div>
        )
    }
}

ReactDOM.render(<Application />, document.getElementById('app'));