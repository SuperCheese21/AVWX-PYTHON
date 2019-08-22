from django.urls import path

from . import views

urlpatterns = [
    path('airports/all/<icao>/', views.airport_detail),
    path('airports/<icao>', views.airport),
    path('frequencies/<icao>', views.frequency),
    path('runways/<icao>', views.runway),
    path('metar/<icao>', views.metar)
]
