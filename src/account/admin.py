from django.contrib import admin

from account.models import UserStatistics
from stationary.admin import ChoiceInline


# Register your models here.
class UserStatisticsAdmin(admin.ModelAdmin):
    fields=['username']
    inlines=[ChoiceInline]
    list_display=('id','username','first_name','is_staff')
    list_filter=['id']
    
admin.site.register(UserStatistics, UserStatisticsAdmin)