from django.urls import path

from . import views

urlpatterns = [
    path('airports/<icao>/', views.airport_detail),
]
