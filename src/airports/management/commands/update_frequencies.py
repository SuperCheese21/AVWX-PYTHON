import requests
from django.core.management.base import BaseCommand
from src.airports.models import Airport, Frequency
from src.airports.db.update_data import update_data


class Command(BaseCommand):
    help = "Updates frequencies database with latest OurAirports data"

    def handle(self, *args, **options):
        url = "http://ourairports.com/data/airport-frequencies.csv"

        print(f"Requesting latest frequency data from {url}...")
        rows = requests.get(url).content.decode().split("\n")[:-1]

        create_new = lambda row: Frequency.objects.create_frequency(
            row,
            Airport
        )
        update_data(rows, Frequency, create_new)
