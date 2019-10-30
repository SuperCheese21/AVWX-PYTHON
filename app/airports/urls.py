from django.urls import path

from . import views

urlpatterns = [
    path('airports/<icao>', views.airport),
    path('airports/info/<icao>', views.info),
    path('airports/frequencies/<icao>', views.frequency),
    path('airports/runways/<icao>', views.runway)
]
