from django.core.management.base import BaseCommand
from airports.models import Airport
from airports.db.update_data import update_data


class Command(BaseCommand):
    help = "Updates airports database with latest OurAirports data"

    def handle(self, *args, **options):
        update_data(
            "http://ourairports.com/data/airports.csv",
            Airport,
            Airport.objects.create_airport,
        )
