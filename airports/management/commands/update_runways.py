from django.core.management.base import BaseCommand
from airports.models import Airport, Runway
from airports.db.update_data import get_runway, update_data


class Command(BaseCommand):
    help = "Updates runways database with latest OurAirports data"

    def handle(self, *args, **options):
        get_new = lambda row: get_runway(row, Runway, Airport)
        update_data("http://ourairports.com/data/runways.csv", Runway, get_new)
