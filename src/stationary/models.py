import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class StationaryType(models.Model):
    name=models.CharField(max_length=100)
    remark=models.CharField(max_length=100,default=None)
    
    def __str__(self):
        return self.name
    
    def sum(self):
        num=0
        for choice in self.choice_set.all():
            num= num+choice.num
        return num
    
class Choice(models.Model):
    user=models.ForeignKey(User)
    stationary_type=models.ForeignKey(StationaryType)
    num=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)
    
    def get_user_name(self):
        return self.user.username
    
    def get_user_stationaryname(self):
        return self.stationary_type.name
    
    def get_user_stationarynum(self):
        return self.stationary_type.num
