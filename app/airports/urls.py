from django.urls import path

from . import views

urlpatterns = [
    path('airports/search', views.AirportSearchView.as_view()),
    path('airports/info/<pk>', views.AirportInfoView.as_view()),
    path('airports/frequencies', views.FrequencyListView.as_view()),
    path('airports/runways', views.RunwayListView.as_view()),
    path('airports/<icao>', views.airport),
]
