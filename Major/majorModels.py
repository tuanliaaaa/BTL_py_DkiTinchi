from django.db import models

# Create your models here.
class Major(models.Model):
    majorName = models.CharField(max_length=255)
    majorCode = models.CharField(max_length=255)

    def __str__(self):
        return self.majorName