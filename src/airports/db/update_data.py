import csv
from decimal import InvalidOperation
from django.core.exceptions import ObjectDoesNotExist


def update_data(rows, model, create_new):
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
