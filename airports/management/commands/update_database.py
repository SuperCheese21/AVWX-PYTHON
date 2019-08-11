import csv
import requests

from airports.models import Airport
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Updates airports database with latest OurAirports data"

    def handle(self, *args, **options):
        data = requests.get('http://ourairports.com/data/airports.csv').text
        Airport.objects.all().delete()
        reader = csv.reader(data.split('\n'))
        for row in reader:
            icao = row[1]
            print(f'Adding {icao}')
