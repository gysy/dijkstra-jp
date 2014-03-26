#-*- coding: UTF-8 -*- 
from django.contrib import admin
from django.db import models
from django.utils.encoding import smart_text

from signup.models import Examsignup


# Create your models here.
class Examscore(models.Model):
    examsignup = models.ForeignKey(Examsignup)
    score = models.IntegerField()
    def __unicode__(self):
        return smart_text('%s 成绩为 %i' % (self.examsignup, self.score))
    
class ExamscoreAdmin(admin.ModelAdmin):
    list_display = ('examsignup', 'score')
    search_fields = ['user']
    
admin.site.register(Examscore, ExamscoreAdmin)
