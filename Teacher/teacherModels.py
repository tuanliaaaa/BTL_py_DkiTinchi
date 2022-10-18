from django.db import models
from Account.accountModels import Account
class Teacher(models.Model):
    teacherCode = models.CharField(max_length=255)
    email = models.EmailField()
    userID = models.ForeignKey(Account,on_delete=models.CASCADE)
    
    