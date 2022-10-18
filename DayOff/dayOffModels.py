from django.db import models

# Create your models here.
class DayOff(models.Model):
    dayOff = models.DateField()