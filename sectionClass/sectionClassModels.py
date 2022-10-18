from tkinter import CASCADE
from django.db import models
from Teacher.teacherModels import Teacher
from Subject.subjectModels import Subject
# Create your models here.
class sectionClass(models.Model):
    subjectID = models.ForeignKey(Subject,on_delete=models.CASCADE)
    teacherID = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    dayStart = models.DateField()
    quanlity = models.IntegerField()
    