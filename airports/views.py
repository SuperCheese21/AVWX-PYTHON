from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from airports.metar import get_metar_data
from airports.models import Airport, Frequency, Runway
from airports.serializers import AirportSerializer, FrequencySerializer, RunwaySerializer


@csrf_exempt
def airport_detail(request, icao):
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
    metar_data = get_metar_data(icao)

    airport_serializer = AirportSerializer(airport_data)
    frequency_serializer = FrequencySerializer(frequency_data, many=True)
    runway_serializer = RunwaySerializer(runway_data, many=True)
    return JsonResponse({
        'info': airport_serializer.data,
        'frequencies': frequency_serializer.data,
        'runways': runway_serializer.data,
        'metar': metar_data
    })


@csrf_exempt
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

    airport_serializer = AirportSerializer(airport_data)
    return JsonResponse({
        'info': airport_serializer.data
    })


@csrf_exempt
def frequency(request, icao):
    if request.method != 'GET':
        return JsonResponse({
            "message": f"Invalid HTTP method"
        }, status=405)

    frequency_data = Frequency.objects.filter(icao=icao).all()
    frequency_serializer = FrequencySerializer(frequency_data, many=True)
    return JsonResponse({
        'frequencies': frequency_serializer.data
    })


@csrf_exempt
def runway(request, icao):
    if request.method != 'GET':
        return JsonResponse({
            "message": f"Invalid HTTP method"
        }, status=405)

    runway_data = Runway.objects.filter(icao=icao).all()
    runway_serializer = RunwaySerializer(runway_data, many=True)
    return JsonResponse({
        'runways': runway_serializer.data
    })


@csrf_exempt
def metar(request, icao):
    if request.method != 'GET':
        return JsonResponse({
            "message": f"Invalid HTTP method"
        }, status=405)

    metar_data = get_metar_data(icao)
    return JsonResponse({
        'metar': metar_data
    })
