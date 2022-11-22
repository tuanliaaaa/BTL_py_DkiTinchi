from django.db import models
from Term.termModels import Term
from SubjectMajor.subjectMajormodels import SubjectMajor
# Create your models here.
class TermMajorSubject(models.Model):
    term = models.ForeignKey(Term,on_delete=models.CASCADE)
    majorSubject = models.ForeignKey(SubjectMajor,on_delete=models.CASCADE)
    