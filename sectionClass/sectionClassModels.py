from tkinter import CASCADE
from django.db import models
from Teacher.teacherModels import Teacher
from SubjectMajor.subjectMajormodels import SubjectMajor
from Term.termModels import Term
from datetime import date,timedelta,datetime
# Create your models here.
class sectionClass(models.Model):
    subjectMajor = models.ForeignKey(SubjectMajor,on_delete=models.CASCADE)
    teacherID = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    quanlity = models.IntegerField()
    quanlityReal = models.IntegerField(null=True)
    dayDefault = models.CharField(max_length=255,null=True)
    dayLessonList = models.CharField(max_length=1000000000,null=True,blank=True)
    term = models.ForeignKey(Term,on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
        if self.dayDefault:
            dayLessonList=[]
            daysDefaultList=self.dayDefault.split(",")
            for dayDefault in daysDefaultList:
                d=int(dayDefault[0])-2
                day=d-self.term.dayStart.weekday()
                if day<0:
                    day+=6
                startx=self.term.dayStart+timedelta(days=day)
                begin=0
                while(True):
                    begin =dayDefault[dayDefault.find("(")+1:-1].find("1", begin,len(dayDefault[dayDefault.find("(")+1:-1]))
                    if(begin==-1):
                        break
                    else:
                        dayLessonList.append((startx+timedelta(days=begin*7)).strftime("%Y/%m/%d")+"("+dayDefault[:dayDefault.find("(")]+")")
                        begin+=1
            dayLessonList.sort(key=lambda x:datetime.strptime(x[:10], "%Y/%m/%d"))
            self.dayLessonList=" ".join(dayLessonList)
        super().save(*args, **kwargs)

    