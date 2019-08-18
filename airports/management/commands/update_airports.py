import requests
from django.core.management.base import BaseCommand
from airports.models import Airport
from airports.db.update_data import update_data


class Command(BaseCommand):
    help = "Updates airports database with latest OurAirports data"

    def handle(self, *args, **options):
        url = "http://ourairports.com/data/airports.csv"

        print(f"Requesting latest airports data from {url}...")
        rows = requests.get(url).text.split("\n")

        update_data(rows, Airport, Airport.objects.create_airport)
