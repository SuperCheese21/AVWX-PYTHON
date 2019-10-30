import React, { Component } from 'react';
import axios from 'axios';
import { Spinner } from 'react-bootstrap';

import Header from './Header';
import RunwayDiagram from './RunwayDiagram';
import './index.css';

export default class Airport extends Component {
  state = {
    data: null
  };

  async componentDidMount() {
    const {
      match: {
        params: { icao }
      }
    } = this.props;
    const { data } = await axios.get(`/api/airports/${icao}`);
    this.setState({ data });
  }

  render() {
    if (!this.state.data) {
      return (
        <div className="loading-container">
          <Spinner animation="border" role="status">
            <span className="sr-only">Loading...</span>
          </Spinner>
        </div>
      );
    }

    const {
      data: { info, runways }
    } = this.state;

    return (
      <>
        <Header
          icao={info.icao}
          iata={info.iata}
          country={info.country}
          municipality={info.municipality}
        />
        <div className="airport-container">
          <RunwayDiagram data={runways}></RunwayDiagram>
        </div>
      </>
    );
  }
}
