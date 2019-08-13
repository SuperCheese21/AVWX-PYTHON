from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from airports.models import Airport


class AirportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airport
        fields = ['icao', 'iata', 'name', 'type', 'latitude', 'longitude', 'elevation_ft', 'continent', 'country', 'region', 'municipality', 'scheduled_service']


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


router = routers.DefaultRouter()
router.register(r'airports', AirportViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
