from django.core.management.base import BaseCommand
from airports.models import Airport, Frequency
from airports.db.update_data import update_data


class Command(BaseCommand):
    help = "Updates frequencies database with latest OurAirports data"

    def handle(self, *args, **options):
        create_new = lambda row: Frequency.objects.create_frequency(
            row, Airport
        )
        update_data(
            "http://ourairports.com/data/airport-frequencies.csv",
            Frequency,
            create_new,
        )
