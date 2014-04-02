from django.contrib import admin
from django.db import models
from django.utils.encoding import smart_text

from signup.models import Examsignup


# Create your models here.
class Examscore(models.Model):
    examsignup = models.ForeignKey(Examsignup)
    vocabulary = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    grammer = models.IntegerField(default=0)
    # def score(self):
    #    return
    def __unicode__(self):
        return smart_text('%s vocabulary_score:%i reading_score:%i grammer_score:%i' % (self.examsignup, self.vocabulary, self.reading, self.grammer))
    
class ExamscoreAdmin(admin.ModelAdmin):
    list_display = ('examsignup', 'vocabulary', 'reading', 'grammer')
        
admin.site.register(Examscore, ExamscoreAdmin)
