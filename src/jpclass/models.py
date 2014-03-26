from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text


class Ngrade(models.Model):
    grade = models.CharField(unique=True, max_length=2)
    def __unicode__(self):
        return self.grade;

class Jpclass(models.Model):
    ngrade = models.ForeignKey(Ngrade)
    classname = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
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

admin.site.register(Ngrade)
admin.site.register(Jpclass, JpclassAdmin)
admin.site.register(Jpclasssubmit, JpclasssubmitAdmin)