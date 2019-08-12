from django.core.management.base import BaseCommand
from airports.models import Airport, Frequency
from airports.db.update_data import get_frequency, update_data


class Command(BaseCommand):
    help = "Updates frequencies database with latest OurAirports data"

    def handle(self, *args, **options):
        get_new = lambda row: get_frequency(row, Frequency, Airport)
        update_data(
            "http://ourairports.com/data/airport-frequencies.csv",
            Frequency,
            get_new,
        )
