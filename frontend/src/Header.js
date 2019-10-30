import React from 'react';

const Header = ({ icao, iata, country, municipality }) => (
  <div className="header-container">
    <img
      className="flag-img"
      src={`https://www.countryflags.io/${country}/flat/64.png`}
      alt={country}
    ></img>
    <h1>
      {icao}/{iata} - {municipality}
    </h1>
  </div>
);

export default Header;
