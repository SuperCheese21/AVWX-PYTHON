import os

from django.core.management.base import BaseCommand
from src.airports.models import Airport, Runway
from src.airports.db.update_data import update_data


class Command(BaseCommand):
    help = "Updates runways database from latest runways.csv file"

    def handle(self, *args, **options):
        path = os.path.dirname(os.path.realpath(__file__)) + "/../../db/"

        with open(path + "runways.csv", "r") as runway_data:
            rows = runway_data.read().split("\n")[:-1]
            create_new = lambda row: Runway.objects.create_runway(row, Airport)
            update_data(rows, Runway, create_new)
