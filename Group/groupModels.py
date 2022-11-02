from django.db import models

# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=255) 