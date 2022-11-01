import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category , State , Iso , Region , Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header


    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()
    Region.objects.all().delete()

    for row in reader:

        c , Ccreated = Category.objects.get_or_create(name=row[7])
        s , Screated = State.objects.get_or_create(name=row[8])
        r , Rcreated = Region.objects.get_or_create(name=row[9])
        i , Icreated = Iso.objects.get_or_create(name=row[10])




        try:
            year = int(row[3])
        except:
            year = None

        try:
            longitude = float(row[4])
        except:
            longitude = None

        try:
            latitude = float(row[5])
        except:
            latitude = None

        try:
            area= float(row[6])
        except:
            area = None

        site = Site(name=row[0], description=row[1], justification=row[2],  year= year, longitude=longitude, latitude=latitude, area_hectares= area, category=c, state=s, region=r, iso=i)
        site.save()



    print("Database Populated Successfully!\nExited...")
