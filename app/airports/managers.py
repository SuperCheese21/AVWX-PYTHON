from django.db import models


class AirportManager(models.Manager):
    def create_airport(self, row):
        return self.create(
            icao=row[1],
            iata=row[13],
            type=row[2],
            name=row[3],
            latitude=row[4] or None,
            longitude=row[5] or None,
            elevation_ft=row[6] or None,
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
            frequency=row[5] or None,
        )


class RunwayManager(models.Manager):
    def create_runway(self, row, airport):
        return self.create(
            icao=airport.objects.get(icao=row[0]),
            length_ft=row[1] or None,
            width_ft=row[2] or None,
            surface=row[3],
            le_ident=row[4],
            le_latitude=row[5] or None,
            le_longitude=row[6] or None,
            le_elevation_ft=row[7] or None,
            le_displaced_ft=row[8] or None,
            he_ident=row[9],
            he_latitude=row[10] or None,
            he_longitude=row[11] or None,
            he_elevation_ft=row[12] or None,
            he_displaced_ft=row[13] or None,
        )
