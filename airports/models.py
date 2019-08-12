from django.db import models


class Airport(models.Model):
    icao = models.CharField(max_length=8, primary_key=True)
    iata = models.CharField(max_length=3)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    elevation_ft = models.IntegerField(blank=True)
    continent = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=16)
    municipality = models.CharField(max_length=128)
    scheduled_service = models.BooleanField(default=False)

    def __str__(self):
        return self.icao


class Frequency(models.Model):
    icao = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    frequency = models.DecimalField(max_digits=7, decimal_places=3)

    def __str__(self):
        return f"{self.icao} {self.type} ({self.frequency})"


class Runway(models.Model):
    icao = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    length_ft = models.IntegerField(blank=True)
    width_ft = models.IntegerField(blank=True)
    surface = models.CharField(max_length=64)
    lighted = models.BooleanField(blank=True)
    closed = models.BooleanField(blank=True)
    le_ident = models.CharField(max_length=8)
    le_latitude = models.FloatField(blank=True)
    le_longitude = models.FloatField(blank=True)
    le_elevation_ft = models.IntegerField(blank=True)
    le_heading_true = models.DecimalField(blank=True, max_digits=4, decimal_places=1)
    le_displaced_threshold_ft = models.IntegerField(blank=True)
    he_ident = models.CharField(max_length=8)
    he_latitude = models.FloatField(blank=True)
    he_longitude = models.FloatField(blank=True)
    he_elevation_ft = models.IntegerField(blank=True)
    he_heading_true = models.DecimalField(blank=True, max_digits=4, decimal_places=1)
    he_displaced_threshold_ft = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.icao} {self.le_ident}/{self.he_ident} ({self.length_ft})"
