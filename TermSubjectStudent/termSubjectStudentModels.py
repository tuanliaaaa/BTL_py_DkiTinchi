from django.db import models
from Student.studentModels import Student
from TermMajorSubject.termMajorSubjectModels import TermMajorSubject
# Create your models here.
class TermSubjectStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    termMajorSubject = models.ForeignKey(TermMajorSubject,on_delete=models.CASCADE)
    

