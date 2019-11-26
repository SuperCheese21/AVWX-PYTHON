from django.http import JsonResponse
from rest_framework import filters, generics

from app.airports.models import Airport, Frequency, Runway
from app.airports.serializers import AirportSearchSerializer, InfoSerializer, FrequencySerializer, RunwaySerializer


def airport(request, icao):
    if request.method != 'GET':
        return JsonResponse({
            "message": f"Invalid HTTP method"
        }, status=405)

    try:
        airport_data = Airport.objects.get(icao=icao)
    except Airport.DoesNotExist:
        return JsonResponse({
            "message": f"No airports matching '{icao}' were found"
        }, status=404)

    frequency_data = Frequency.objects.filter(icao=icao).all()
    runway_data = Runway.objects.filter(icao=icao).all()

    info_serializer = InfoSerializer(airport_data)
    frequency_serializer = FrequencySerializer(frequency_data, many=True)
    runway_serializer = RunwaySerializer(runway_data, many=True)
    return JsonResponse({
        'info': info_serializer.data,
        'frequencies': frequency_serializer.data,
        'runways': runway_serializer.data
    })


class AirportInfoView(generics.RetrieveAPIView):
    queryset = Airport.objects.all()
    serializer_class = InfoSerializer


class FrequencyListView(generics.ListAPIView):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=icao']


class RunwayListView(generics.ListAPIView):
    queryset = Runway.objects.all()
    serializer_class = RunwaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=icao']


class AirportSearchView(generics.ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSearchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^icao', '^iata', 'name', 'municipality']
    ordering = ['-scheduled_service', 'icao']
