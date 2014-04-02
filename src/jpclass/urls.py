from django.conf.urls import patterns, include, url
from django.contrib import admin

from jpclass import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index,name="index"),
    url(r'^submit/$', views.submit,name="submit"),
    url(r'^result/$', views.result,name="result"),
)
