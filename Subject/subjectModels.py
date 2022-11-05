from operator import mod
from django.db import models

# Create your models here.
class Subject(models.Model):
    SubjectCode = models.CharField(max_length=255)
    SubjectName = models.CharField(max_length=255)


    def __str__(self):
        return self.SubjectName
