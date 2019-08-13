import csv
from decimal import InvalidOperation
from django.core.exceptions import ObjectDoesNotExist
import requests


def update_data(url, model, create_new):
    print(f"Requesting latest data from {url}...")
    rows = requests.get(url).text.split("\n")[:-1]

    print("Wiping database table...")
    model.objects.all().delete()

    reader = csv.reader(rows)
    next(reader)
    for row in reader:
        try:
            new = create_new(row)
            new.save()
            print(f"Added {new} ({reader.line_num}/{len(rows)})")
        except InvalidOperation:
            print(f"  {new} - Number formatting error!")
        except ObjectDoesNotExist:
            print(f"  {new} - Foreign key not found!")
        except KeyboardInterrupt:
            print("Terminating database update...")
            exit()
