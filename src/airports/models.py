from django.db import models

from .managers import AirportManager, FrequencyManager, RunwayManager


class Airport(models.Model):
    icao = models.CharField(max_length=8, primary_key=True)
    iata = models.CharField(max_length=3)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    elevation_ft = models.IntegerField(null=True)
    continent = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=16)
    municipality = models.CharField(max_length=128)
    scheduled_service = models.BooleanField(null=True)

    objects = AirportManager()

    def __str__(self):
        return self.icao


class Frequency(models.Model):
    icao = models.CharField(max_length=8)
    type = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    frequency = models.DecimalField(null=True, max_digits=7, decimal_places=3)

    objects = FrequencyManager()

    def __str__(self):
        return f"{self.icao} {self.type} ({self.frequency})"


class Runway(models.Model):
    icao = models.CharField(max_length=8)
    length_ft = models.IntegerField(null=True)
    width_ft = models.IntegerField(null=True)
    surface = models.CharField(max_length=32)
    le_ident = models.CharField(max_length=8)
    le_latitude = models.FloatField(null=True)
    le_longitude = models.FloatField(null=True)
    le_elevation_ft = models.FloatField(null=True)
    le_displaced_ft = models.IntegerField(null=True)
    he_ident = models.CharField(max_length=8)
    he_latitude = models.FloatField(null=True)
    he_longitude = models.FloatField(null=True)
    he_elevation_ft = models.FloatField(null=True)
    he_displaced_ft = models.IntegerField(null=True)

    objects = RunwayManager()

    def __str__(self):
        return f"{self.icao} {self.le_ident}/{self.he_ident} ({self.length_ft})"
