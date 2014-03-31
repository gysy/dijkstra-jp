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
<<<<<<< HEAD
    url(r'^jpclass/', include('jpclass.urls',namespace='jpclass')),
=======
    url(r'^signup/', include('signup.urls',namespace='signup')),
>>>>>>> 3ca99446ffaf39fd9cd809720bfa6de4da3595a6
)
