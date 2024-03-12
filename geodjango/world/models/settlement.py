from django.contrib.gis.db import models
from django.contrib.gis.geos import Polygon

class Settlement(models.Model):
    day_measured = models.DateField()
    identifier = models.IntegerField()
    location = models.PointField(srid=4326)
    municipality = models.CharField(max_length=100)
    settlement = models.CharField(max_length=100)
    hours_of_service = models.CharField(max_length=100)
    supply_zone = models.CharField(max_length=100)
    is_atypical_condition = models.BooleanField()