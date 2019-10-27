import React, { Component } from 'react';

import Two from 'two.js';
import colors from './colors.json';
import { EARTH_RADIUS_FEET } from './constants.json';

import './index.css';

const DEG_TO_RAD = Math.PI / 180;

const MAX_SIZE = 500;
const PADDING = 12;
const TEXT_OFFSET = 7;

export default class RunwayDiagram extends Component {
  componentDidMount() {
    const { data } = this.props;

    const { runwayCoords, viewportDimensions } = this.getNormalizedCoords(data);

    const elem = document.getElementById('runway-diagram');
    const two = new Two(viewportDimensions).appendTo(elem);

    runwayCoords.forEach(({ ident, coords, width, surface }) => {
      const line = new Two.Line(...coords);
      const stroke = this.getRunwayColor(surface);
      line.linewidth = width;
      line.stroke = stroke;

      const {
        heTransformation,
        leTransformation
      } = this.getTextTransformations(coords);

      const heText = new Two.Text(ident.he, ...heTransformation.position);
      heText.rotation = heTransformation.rotation;
      heText.weight = 700;
      heText.size = 10;

      const leText = new Two.Text(ident.le, ...leTransformation.position);
      leText.rotation = leTransformation.rotation;
      leText.weight = 700;
      leText.size = 10;

      two.add(line, heText, leText);
    });

    two.update();
  }

  getNormalizedCoords(runways) {
    const { minLat, maxLat, minLon, maxLon } = this.getEdgeCoords(runways);

    const midLat = (maxLat + minLat) / 2;

    const latLengthFeet = EARTH_RADIUS_FEET * DEG_TO_RAD;
    const lonLengthFeet =
      EARTH_RADIUS_FEET * DEG_TO_RAD * Math.cos(midLat * DEG_TO_RAD);

    const heightFeet = latLengthFeet * (maxLat - minLat);
    const widthFeet = lonLengthFeet * (maxLon - minLon);

    const feetToPixels =
      (MAX_SIZE - 2 * PADDING) / Math.max(heightFeet, widthFeet);

    const viewportDimensions = {
      height: feetToPixels * heightFeet + 2 * PADDING,
      width: feetToPixels * widthFeet + 2 * PADDING
    };

    const runwayCoords = runways.map(runway => {
      const heLatFeet = latLengthFeet * (maxLat - runway.he_latitude);
      const heLonFeet = lonLengthFeet * (runway.he_longitude - minLon);
      const leLatFeet = latLengthFeet * (maxLat - runway.le_latitude);
      const leLonFeet = lonLengthFeet * (runway.le_longitude - minLon);
      return {
        ident: {
          he: runway.he_ident,
          le: runway.le_ident
        },
        coords: [heLonFeet, heLatFeet, leLonFeet, leLatFeet].map(
          feet => feetToPixels * feet + PADDING
        ),
        width: feetToPixels * runway.width_ft,
        surface: runway.surface
      };
    });

    return {
      runwayCoords,
      viewportDimensions
    };
  }

  getEdgeCoords(data) {
    const latitudes = data.flatMap(runway => [
      runway.le_latitude,
      runway.he_latitude
    ]);
    const longitudes = data.flatMap(runway => [
      runway.le_longitude,
      runway.he_longitude
    ]);

    return {
      minLat: Math.min(...latitudes),
      maxLat: Math.max(...latitudes),
      minLon: Math.min(...longitudes),
      maxLon: Math.max(...longitudes)
    };
  }

  getRunwayColor(surface) {
    const { runways: runwayColors } = colors;
    if (surface.includes('Asphalt')) {
      return runwayColors.asphalt;
    } else if (surface.includes('Dirt') || surface.includes('Clay')) {
      return runwayColors.dirt;
    } else if (surface.includes('Gravel') || surface.includes('Grvl')) {
      return runwayColors.gravel;
    } else if (
      surface.includes('Turf') ||
      surface.includes('Grass') ||
      surface.includes('Soft')
    ) {
      return runwayColors.grass;
    } else if (surface.includes('Water')) {
      return runwayColors.water;
    }

    return runwayColors.concrete;
  }

  getTextTransformations(coords) {
    const dx = coords[2] - coords[0];
    const dy = coords[1] - coords[3];

    const heRotation = Math.atan2(dx, dy);
    const leRotation = heRotation + Math.PI;

    const hePosition = [
      coords[0] - TEXT_OFFSET * Math.sin(heRotation),
      coords[1] + TEXT_OFFSET * Math.cos(heRotation)
    ];
    const lePosition = [
      coords[2] - TEXT_OFFSET * Math.sin(leRotation),
      coords[3] + TEXT_OFFSET * Math.cos(leRotation)
    ];

    return {
      heTransformation: {
        position: hePosition,
        rotation: heRotation
      },
      leTransformation: {
        position: lePosition,
        rotation: leRotation
      }
    };
  }

  render() {
    return <div id="runway-diagram"></div>;
  }
}
