from django.contrib import admin

from stationary.models import Choice, StationaryType


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
 
class StationaryAdmin(admin.ModelAdmin):
    fieldsets = [
              (None, {'fields': ['name']}),
              ('Remark information', {'fields': ['remark'], 'classes': ['collapse']}),
         ]
    inlines = [ChoiceInline]
    list_display = ('name', 'remark', 'sum',)
    list_filter = ['name']
      
admin.site.register(StationaryType, StationaryAdmin)
