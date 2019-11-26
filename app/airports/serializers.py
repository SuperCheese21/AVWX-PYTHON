from rest_framework import serializers

from app.airports.models import Airport, Frequency, Runway


class AirportSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['icao', 'iata', 'name', 'country', 'municipality']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        exclude = ['id', 'icao']


class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        exclude = ['id', 'icao']
