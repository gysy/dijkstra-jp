#-*- coding: UTF-8 -*- 
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text


class Ngrade(models.Model):
    grade = models.CharField(unique=True, max_length=5)
    def __unicode__(self):
        return self.grade
    
class Jpclass(models.Model):
    ngrade = models.ForeignKey(Ngrade)
    classname = models.CharField(max_length=10)
    
    def __unicode__(self):
        return smart_text('Classname:%s %s' % (self.classname, self.ngrade))
    
class JpclassAdmin(admin.ModelAdmin):
    list_display = ('id', 'ngrade', 'classname')
    list_filter = ['ngrade']

class Jpclasssubmit(models.Model):
    user = models.ForeignKey(User)
    jpclass = models.ForeignKey(Jpclass)
    def __unicode__(self):
        return smart_text('%s has signed up  %s' % (self.user, self.jpclass))
    
class JpclasssubmitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'jpclass')
    search_fields = ['user']


class Examdate(models.Model):
    month = models.IntegerField()
    year = models.IntegerField(default = 0)
    def __unicode__(self):
        return smart_text('%s %s' % (str(self.month), str(self.year)))


class Examsignup(models.Model):
    user=models.ForeignKey(User)
    ngrade = models.ForeignKey(Ngrade)
    examdate = models.ForeignKey(Examdate)
    def __unicode__(self):
        return smart_text('%s %s %s' % (self.user, self.examdate, self.ngrade))

class ExamsignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'ngrade', 'examdate', 'examdate')
    list_filter = ['ngrade']
    
class Examscore(models.Model):
    examsignup = models.ForeignKey(Examsignup)
    vocabulary = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    grammar = models.IntegerField(default=0)
    def __unicode__(self):
        return smart_text('%s vocabulary_score:%i reading_score:%i grammer_score:%i' % (self.examsignup, self.vocabulary, self.reading, self.grammar))
    
class ExamscoreAdmin(admin.ModelAdmin):
    list_display = ('examsignup', 'vocabulary', 'reading', 'grammar')
        
admin.site.register(Examscore, ExamscoreAdmin)

admin.site.register(Examdate)
admin.site.register(Examsignup, ExamsignupAdmin)

admin.site.register(Ngrade)
admin.site.register(Jpclass, JpclassAdmin)
admin.site.register(Jpclasssubmit, JpclasssubmitAdmin)
