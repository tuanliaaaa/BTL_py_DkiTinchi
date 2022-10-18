from django.db import models
from sectionClass.sectionClassModels import sectionClass
from Student.studentModels import Student
# Create your models here.
class sectionClassStudent(models.Model):
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE)
    sectionClassID = models.ForeignKey(sectionClass,on_delete=models.CASCADE)
