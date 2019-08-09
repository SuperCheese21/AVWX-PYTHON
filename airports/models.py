from django.db import models

# Create your models here.
class Airport(models.Model):
    icao = models.CharField(max_length=4, primary_key=True)
    iata = models.CharField(max_length=3)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    elevation_ft = models.IntegerField(default=0)
    continent = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    region = models.CharField(max_length=16)
    municipality = models.CharField(max_length=128)
    scheduled_service = models.BooleanField(default=False)

    def __str__(self):
        return self.icao
