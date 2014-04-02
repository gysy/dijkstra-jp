from django.contrib import admin
from django.db import models
from django.utils.encoding import smart_text

from signup.models import Examsignup,ExamsignupSubmit


# Create your models here.
class Examscore(models.Model):
    examsignupsubmit = models.ForeignKey(ExamsignupSubmit)
    vocabulary = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    grammer = models.IntegerField(default=0)
    # def score(self):
    #    return
    def __unicode__(self):
        return smart_text('%s vocabulary_score:%i reading_score:%i grammer_score:%i' % (self.examsignupsubmit, self.vocabulary, self.reading, self.grammer))
    
class ExamscoreAdmin(admin.ModelAdmin):
    list_display = ('examsignupsubmit', 'vocabulary', 'reading', 'grammer')
        
admin.site.register(Examscore, ExamscoreAdmin)
