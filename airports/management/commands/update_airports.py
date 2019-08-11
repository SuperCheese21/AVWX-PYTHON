import csv
import requests

from airports.models import Airport
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Updates airports database with latest OurAirports data'

    def handle(self, *args, **options):
        url = 'http://ourairports.com/data/airports.csv'
        print(f'Requesting latest airports file from {url}...')
        rows = requests.get(url).text.split('\n')
        num_airports = len(rows)

        print('Wiping database...')
        Airport.objects.all().delete()

        reader = csv.reader(rows)
        next(reader)
        for row in reader:
            airport = Airport(
                icao=row[1],
                iata=row[13],
                type=row[2],
                name=row[3],
                latitude=row[4],
                longitude=row[5],
                elevation_ft=row[6] or '0',
                continent=row[7],
                country=row[8],
                region=row[9],
                municipality=row[10],
                scheduled_service=True if row[11] == 'yes' else False
            )
            airport.save()
            print(f'Added {airport} ({reader.line_num}/{num_airports})')
