from django.db import models
from Account.accountModels import Account
from Group.groupModels import Group

# Create your models here.
class AccountGroup(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.account.username +"-"+self.group.groupName