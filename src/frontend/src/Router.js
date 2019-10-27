import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Airport from './Airport';

const Router = () => (
  <BrowserRouter>
    <div className="main-container">
      <Route path="/:icao" component={Airport} />
    </div>
  </BrowserRouter>
);

export default Router;
