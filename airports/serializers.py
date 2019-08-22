from rest_framework import serializers

from airports.models import Airport, Frequency, Runway


class AirportSerializer(serializers.ModelSerializer):
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
