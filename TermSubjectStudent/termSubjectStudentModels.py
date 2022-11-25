from django.db import models
from Student.studentModels import Student
from Term.termModels import Term
from SubjectMajor.subjectMajormodels import SubjectMajor
# Create your models here.
class TermSubjectStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    term = models.ForeignKey(Term,on_delete=models.CASCADE,null=True)
    subjectMajor = models.ForeignKey(SubjectMajor,on_delete=models.CASCADE,null=True)
    
    def save(self, *args, **kwargs):
        if TermSubjectStudent.objects.filter(student=self.student,term=self.term,subjectMajor= self.subjectMajor):
            return
        else:super().save(*args, **kwargs)