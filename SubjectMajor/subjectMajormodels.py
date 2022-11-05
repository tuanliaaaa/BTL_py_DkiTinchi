from django.db import models
from Major.majorModels import Major
from Subject.subjectModels import Subject
# Create your models here.
class SubjectMajor(models.Model):
    major = models.ForeignKey(Major,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    numberOfCredits = models.IntegerField()
    startTerm = models.IntegerField()
