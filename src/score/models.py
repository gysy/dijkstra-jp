#-*- coding: UTF-8 -*- 
from django.contrib import admin
from django.db import models
from django.utils.encoding import smart_text

from signup.models import Examsignup,ExamsignupSubmit


# Create your models here.
class Examscore(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
    examsignup = models.ForeignKey(ExamsignupSubmit)
=======
    examsignupsubmit = models.ForeignKey(ExamsignupSubmit)
>>>>>>> ea20db05f311bba2c5e6db0da045337bc14824cd
    vocabulary = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    grammer = models.IntegerField(default=0)
    # def score(self):
    #    return
    def __unicode__(self):
<<<<<<< HEAD
        return smart_text('%s vocabulary_score:%i reading_score:%i grammer_score:%i' % (self.examsignup, self.vocabulary, self.reading, self.grammer))
=======
    examsignup = models.ForeignKey(Examsignup)
    score = models.IntegerField()
    def __unicode__(self):
        return smart_text('%s 成绩为 %i' % (self.examsignup, self.score))
>>>>>>> 846b1a0d305c601b331e47061711359412ec2f64
=======
        return smart_text('%s vocabulary_score:%i reading_score:%i grammer_score:%i' % (self.examsignupsubmit, self.vocabulary, self.reading, self.grammer))
>>>>>>> ea20db05f311bba2c5e6db0da045337bc14824cd
    
class ExamscoreAdmin(admin.ModelAdmin):
    list_display = ('examsignupsubmit', 'vocabulary', 'reading', 'grammer')
        
admin.site.register(Examscore, ExamscoreAdmin)
