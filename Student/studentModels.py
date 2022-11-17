from django.db import models
from Account.accountModels import Account
class Student(models.Model):
    studentCode = models.CharField(max_length=255)
    email = models.EmailField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255)
    
    