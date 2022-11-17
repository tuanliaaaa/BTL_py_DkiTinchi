from tkinter import CASCADE
from django.db import models
from Teacher.teacherModels import Teacher
from SubjectMajor.subjectMajormodels import SubjectMajor
# Create your models here.
class sectionClass(models.Model):
    subjectMajor = models.ForeignKey(SubjectMajor,on_delete=models.CASCADE)
    teacherID = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    dayStart = models.DateField()
    quanlity = models.IntegerField()
    quanlityReal = models.IntegerField(null=True)
    dayDefault = models.CharField(max_length=255,null=True)
    dayAdd = models.IntegerField(null=True)
    dayLessonList = models.IntegerField(null=True)
    dayEnd = models.DateField(null=True)
    