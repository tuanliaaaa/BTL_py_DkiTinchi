from django.db import models
from sectionClass.sectionClassModels import sectionClass
from Student.studentModels import Student
# Create your models here.
class sectionClassStudent(models.Model):
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE)
    sectionClassID = models.ForeignKey(sectionClass,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if self.pk:
            return
        if self.sectionClassID.quanlityReal>= self.sectionClassID.quanlity:
            return
        else: 
            self.sectionClassID.quanlityReal+=1
            self.sectionClassID.save()
        if sectionClassStudent.objects.filter(studentID=self.studentID,sectionClassID=self.sectionClassID):
            return
        else:super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        self.sectionClassID.quanlityReal-=1
        self.sectionClassID.save()
        super().delete(*args, **kwargs)

