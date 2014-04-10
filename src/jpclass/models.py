#-*- coding: UTF-8 -*- 
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text


class Ngrade(models.Model):
<<<<<<< HEAD
    grade = models.CharField(unique=True, max_length=5)
    def __unicode__(self):
        return self.grade
    
=======
    grade = models.CharField(unique=True, max_length=2)
    def __unicode__(self):
        return self.grade;

>>>>>>> 846b1a0d305c601b331e47061711359412ec2f64
class Jpclass(models.Model):
    ngrade = models.ForeignKey(Ngrade)
    classname = models.CharField(max_length=10)
    
    def __unicode__(self):
<<<<<<< HEAD
        return smart_text('Classname:%s %s' % (self.classname, self.ngrade))
=======
        return smart_text('班级:%s %s' % (self.classname, self.ngrade))
>>>>>>> 846b1a0d305c601b331e47061711359412ec2f64
    
class JpclassAdmin(admin.ModelAdmin):
    list_display = ('id', 'ngrade', 'classname')
    list_filter = ['ngrade']

class Jpclasssubmit(models.Model):
    user = models.ForeignKey(User)
    jpclass = models.ForeignKey(Jpclass)
    def __unicode__(self):
<<<<<<< HEAD
        return smart_text('%s has signed up  %s' % (self.user, self.jpclass))
=======
        return smart_text('%s 报名了  %s' % (self.user, self.jpclass))
>>>>>>> 846b1a0d305c601b331e47061711359412ec2f64
    
class JpclasssubmitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'jpclass')
    search_fields = ['user']

admin.site.register(Ngrade)
admin.site.register(Jpclass, JpclassAdmin)
admin.site.register(Jpclasssubmit, JpclasssubmitAdmin)
