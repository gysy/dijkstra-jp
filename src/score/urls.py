from django.conf.urls import patterns, include, url
from django.contrib import admin

from score import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^submit/$',views.submit,name="submit"),
    url(r'^result/$',views.result,name="result"),
)
