from django.core.management.base import BaseCommand
from airports.models import Airport, Runway
from airports.db.update_data import update_data


class Command(BaseCommand):
    help = "Updates runways database with latest OurAirports data"

    def handle(self, *args, **options):
        create_new = lambda row: Runway.objects.create_runway(row, Airport)
        update_data(
            "http://ourairports.com/data/runways.csv", Runway, create_new
        )
