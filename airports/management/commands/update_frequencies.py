import csv
import requests

from airports.models import Airport, Frequency
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Updates frequencies database with latest OurAirports data'

    def handle(self, *args, **options):
        url = 'http://ourairports.com/data/airport-frequencies.csv'
        print(f'Requesting latest frequencies file from {url}...')
        rows = requests.get(url).text.split('\n')
        num_frequencies = len(rows)

        print('Wiping frequencies from database...')
        Frequency.objects.all().delete()

        reader = csv.reader(rows)
        next(reader)
        for row in reader:
            frequency = Frequency(
                icao=Airport.objects.get(icao=row[2]),
                type=row[3],
                description=row[4],
                frequency=row[5]
            )
            frequency.save()
            print(f'Added {frequency} ({reader.line_num}/{num_frequencies})')
