from django.db import models

# Create your models here.
class Term(models.Model):
    termName = models.CharField(max_length=255)
    StartTimeSignTerm = models.DateTimeField()
    EndTimeSignTerm = models.DateTimeField()
    StartTimeSignSubject = models.DateTimeField()
    EndTimeSignSubject = models.DateTimeField()

    def save(self, *args, **kwargs):
        if (self.EndTimeSignTerm>self.StartTimeSignTerm 
            and self.StartTimeSignSubject>self.EndTimeSignTerm
            and self.EndTimeSignSubject>self.StartTimeSignSubject):
            super().save(*args, **kwargs)