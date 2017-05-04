from django.db import models
#from django.template.defaultfilters import slugify


class Rain(models.Model):
	#PK automatically handled by django
	station = models.CharField(max_length=30)
	station_name = models.CharField(max_length=30)
	
class RainData(models.Model):
	#PK automatically handled by django
	ddate = models.DateField() #date rain gage measurement was taken
	prcp = models.DecimalField(max_digits=5, decimal_places=2)
	rain = models.ForeignKey(Rain, on_delete=models.CASCADE )#FK
