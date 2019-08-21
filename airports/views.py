from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from airports.models import Airport, Frequency, Runway
from airports.serializers import AirportSerializer, FrequencySerializer, RunwaySerializer


@csrf_exempt
def airport_detail(request, icao):
    try:
        airport = Airport.objects.get(icao=icao)
    except Airport.DoesNotExist:
        return JsonResponse({
            "message": f"No airports matching '{icao}' were found"
        }, status=404)

    frequencies = Frequency.objects.filter(icao=icao).all()
    runways = Runway.objects.filter(icao=icao).all()

    if request.method == 'GET':
        airport_serializer = AirportSerializer(airport)
        frequency_serializer = FrequencySerializer(frequencies, many=True)
        runway_serializer = RunwaySerializer(runways, many=True)
        return JsonResponse({
            'info': airport_serializer.data,
            'frequencies': frequency_serializer.data,
            'runways': runway_serializer.data
        })
