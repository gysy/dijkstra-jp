from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text

from jpclass.models import Ngrade


class Examdate(models.Model):
    date = models.CharField(unique=True, max_length=10)
    def __unicode__(self):
        return self.date



class Examsignup(models.Model):
    ngrade = models.ForeignKey(Ngrade)
    examdate = models.ForeignKey(Examdate)
    def __unicode__(self):
        return smart_text('%s %s' % (self.examdate, self.ngrade))

class ExamsignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'ngrade', 'examdate')
    list_filter = ['ngrade']
    
class ExamsignupSubmit(models.Model):
    user=models.ForeignKey(User)
    examsignup=models.ForeignKey(Examsignup)
#    ngrade=models.ForeignKey(Ngrade)
#    examdate=models.ForeignKey(Examdate)
    def __unicode__(self):
        return smart_text('%s %s %s' % (self.user, self.examsignup.examdate, self.examsignup.ngrade))
    
class ExamsignupSubmitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'examsignup')
    search_field=['user']


admin.site.register(Examdate)
admin.site.register(Examsignup, ExamsignupAdmin)
admin.site.register(ExamsignupSubmit,ExamsignupSubmitAdmin)
