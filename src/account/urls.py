from django.conf.urls import patterns, include, url
from django.contrib import admin

from account import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name="index"),
    url(r'^login/$', views.login,name="login"),
    url(r'^logout/$', views.logout,name="logout"),
)
