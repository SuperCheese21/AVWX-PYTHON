from django.urls import path

from . import views

urlpatterns = [
    path('airports/search', views.AirportSearchView.as_view()),
    path('airports/info/<icao>', views.info),
    path('airports/frequencies/<icao>', views.frequency),
    path('airports/runways/<icao>', views.runway),
    path('airports/<icao>', views.airport),
]
