from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text

from jpclass.models import Ngrade


class Examdate(models.Model):
    year = models.IntegerField(unique=True)
    month = models.IntegerField(unique=True)
    def __str__(self):
        return smart_text('%i-%i' % (self.year, self.month))

class ExamdateAdmin(admin.ModelAdmin):
    list_display = ('year', 'month')

class Examsignup(models.Model):
    user = models.ForeignKey(User)
    ngrade = models.ForeignKey(Ngrade)
    examdate = models.ForeignKey(Examdate)
    def __str__(self):
        return smart_text('%s has signed up %s %s' % (self.user, self.examdate, self.ngrade))

class ExamsignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ngrade', 'examdate')
    list_filter = ['ngrade']
    search_fields = ['user']
    
    
admin.site.register(Examdate, ExamdateAdmin)
admin.site.register(Examsignup, ExamsignupAdmin)
