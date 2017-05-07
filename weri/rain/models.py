from django.db import models


# from django.template.defaultfilters import slugify


class Rain(models.Model):
    # PK automatically handled by django
    station = models.CharField(max_length=30, primary_key=True)  # I think this is really your primary key looking at
    # the data... unless you are going to rebuild the relationships after you put the data in a database.  This way you
    # should just be able to import your data and not worry about that

    station_name = models.CharField(max_length=30)


class RainData(models.Model):
    # PK automatically handled by django
    ddate = models.DateField()  # date rain gage measurement was taken
    prcp = models.DecimalField(max_digits=5, decimal_places=2)
    rain = models.ForeignKey(Rain, on_delete=models.CASCADE)  # FK
