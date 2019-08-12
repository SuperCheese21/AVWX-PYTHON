import csv
import requests

from airports.models import Airport, Runway
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Updates runways database with latest OurAirports data"

    def handle(self, *args, **options):
        url = "http://ourairports.com/data/runways.csv"
        print(f"Requesting latest runways file from {url}...")
        rows = requests.get(url).text.split("\n")
        num_runways = len(rows)

        print("Wiping runways from database...")
        Runway.objects.all().delete()

        reader = csv.reader(rows)
        next(reader)
        for row in reader:
            runway = Runway(
                icao=Airport.objects.get(icao=row[2]),
                length_ft=row[3],
                width_ft=row[4],
                surface=row[5],
                lighted=True if row[6] == "1" else False,
                closed=True if row[7] == "1" else False,
                le_ident=row[8],
                le_latitude=row[9] or None,
                le_longitude=row[10] or None,
                le_elevation_ft=row[11] or None,
                le_heading_true=row[12] or None,
                le_displaced_threshold_ft=row[13] or None,
                he_ident=row[14],
                he_latitude=row[15] or None,
                he_longitude=row[16] or None,
                he_elevation_ft=row[17] or None,
                he_heading_true=row[18] or None,
                he_displaced_threshold_ft=row[19] or None,
            )
            runway.save()
            print(f"Added {runway} ({reader.line_num}/{num_runways})")
