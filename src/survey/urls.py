from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stationary/', include('stationary.urls',namespace='stationary')),
    url(r'^account/', include('account.urls',namespace='account')),
    url(r'^japanese/', include('japanese.urls',namespace='japanese')),
    )
