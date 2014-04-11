#-*- coding: UTF-8 -*- 
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
	user=models.ForeignKey(User)
	ngrade=models.ForeignKey(Ngrade)
	examdate=models.ForeignKey(Examdate)
	def __unicode__(self):
		return smart_text('%s %s %s' % (self.user, self.examdate, self.ngrade))
	
class ExamsignupAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'ngrade','examdate')
	search_field=['user']


admin.site.register(Examdate)
admin.site.register(Examsignup,ExamsignupAdmin)
