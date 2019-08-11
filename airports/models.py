from django.db import models


class Airport(models.Model):
    icao = models.CharField(max_length=8, primary_key=True)
    iata = models.CharField(max_length=3)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation_ft = models.IntegerField(default=0)
    continent = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=16)
    municipality = models.CharField(max_length=128)
    scheduled_service = models.BooleanField(default=False)

    def __str__(self):
        return self.icao


class Frequency(models.Model):
    icao = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=8)
    description = models.CharField(max_length=128)
    frequency = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return f'{self.icao} {self.type} ({self.frequency})'


class Runway(models.Model):
    icao = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    length_ft = models.IntegerField(default=0)
    width_ft = models.IntegerField(default=0)
    surface = models.CharField(max_length=16)
    lighted = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    le_ident = models.CharField(max_length=8)
    le_latitude = models.FloatField()
    le_longitude = models.FloatField()
    le_elevation_ft = models.IntegerField(default=0)
    le_heading_true = models.DecimalField(max_digits=4, decimal_places=1)
    le_displaced_threshold_ft = models.IntegerField(default=0)
    he_ident = models.CharField(max_length=8)
    he_latitude = models.FloatField()
    he_longitude = models.FloatField()
    he_elevation_ft = models.IntegerField(default=0)
    he_heading_true = models.DecimalField(max_digits=4, decimal_places=1)
    he_displaced_threshold_ft = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.icao} {self.le_ident}/{self.he_ident} ({self.length_ft})'
