from tkinter import CASCADE
from django.db import models
from Teacher.teacherModels import Teacher
from SubjectMajor.subjectMajormodels import SubjectMajor
from TermMajorSubject.termMajorSubjectModels import TermMajorSubject
from datetime import date,timedelta
# Create your models here.
class sectionClass(models.Model):
    subjectMajor = models.ForeignKey(SubjectMajor,on_delete=models.CASCADE)
    teacherID = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    dayStart = models.DateField()
    quanlity = models.IntegerField()
    quanlityReal = models.IntegerField(null=True)
    dayDefault = models.CharField(max_length=255,null=True)
    dayAdd = models.CharField(max_length=100000,null=True)
    dayLessonList = models.CharField(max_length=100000,null=True,blank=True)
    dayEnd = models.DateField(null=True)
    termMajorSubject = models.ForeignKey(TermMajorSubject,on_delete=models.CASCADE,blank=True,null=True)

    def save(self, *args, **kwargs):
        # try:
        #     dayStart= self.dayStart
        #     dem=0
        #     numberOfCredits = self.subjectMajor.numberOfCredits
        #     check=dem*7
        #     self.dayLessonList=""
        #     print(dayStart.weekday()+1)
        #     if(dayStart.weekday()+1==int(self.dayDefault[0])):
        #         print('vclS')
        #     while(dem!=check):
        #         self.dayLessonList = '1'
        # except:
        #     pass
        super().save(*args, **kwargs)

    