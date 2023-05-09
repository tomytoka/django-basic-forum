import csv  # https://docs.python.org/3/library/csv.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        iso, created = Iso.objects.get_or_create(name=row[10])
        sta, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])

        try:
            y = int(row[3])
        except:
            y = None
        try:
            lon = float(row[4])
        except:
            lon = None
        try:
            lat = float(row[5])
        except:
            lat = None
        try:
            ah = float(row[6])
        except:
            ah = None

        site = Site(name=row[0], description=row[1],justification=row[2], year = y,longitude = lon,latitude = lat,area_hectares = ah ,category=cat, state = sta ,region=reg,iso=iso)
        site.save()