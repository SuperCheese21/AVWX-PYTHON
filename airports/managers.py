from django.db import models


class AirportManager(models.Manager):
    def create_airport(self, row):
        return self.create(
            icao=row[1],
            iata=row[13],
            type=row[2],
            name=row[3],
            latitude=row[4],
            longitude=row[5],
            elevation_ft=row[6] or "0",
            continent=row[7],
            country=row[8],
            region=row[9],
            municipality=row[10],
            scheduled_service=row[11] == "yes",
        )


class FrequencyManager(models.Manager):
    def create_frequency(self, row, airport):
        return self.create(
            icao=airport.objects.get(icao=row[2]),
            type=row[3],
            description=row[4],
            frequency=row[5],
        )


class RunwayManager(models.Manager):
    def create_runway(self, row, airport):
        return self.create(
            icao=airport.objects.get(icao=row[2]),
            length_ft=row[3] or None,
            width_ft=row[4] or None,
            surface=row[5],
            lighted=row[6] == "1",
            closed=row[7] == "1",
            le_ident=row[8],
            le_latitude=row[9] or None,
            le_longitude=row[10] or None,
            le_elevation_ft=row[11] or None,
            le_heading_true=row[12] or None,
            le_displaced_threshold_ft=row[13] or None,
            he_ident=row[14],
            he_latitude=row[15] or None,
            he_longitude=row[16] or None,
            he_elevation_ft=row[17] or None,
            he_heading_true=row[18] or None,
            he_displaced_threshold_ft=row[19] or None,
        )
