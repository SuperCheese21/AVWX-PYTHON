import csv
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
        except KeyboardInterrupt:
            print("Stopping database update...")
            model.objects.all().delete()
            exit()
