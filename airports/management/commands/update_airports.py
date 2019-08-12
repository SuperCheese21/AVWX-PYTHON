from django.core.management.base import BaseCommand
from airports.models import Airport
from airports.db.update_data import get_airport, update_data


class Command(BaseCommand):
    help = "Updates airports database with latest OurAirports data"

    def handle(self, *args, **options):
        get_new = lambda row: get_airport(row, Airport)
        update_data(
            "http://ourairports.com/data/airports.csv", Airport, get_new
        )
