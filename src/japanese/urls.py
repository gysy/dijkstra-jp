from django.conf.urls import patterns, include, url
from django.contrib import admin
from japanese import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.japanese_index,name="japanese_index"),
)
