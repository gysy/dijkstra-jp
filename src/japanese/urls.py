from django.conf.urls import patterns, include, url
from django.contrib import admin
from japanese import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jpclass$', views.jpclass_index,name="jpclass_index"),
    url(r'^signup/submit$', views.signup_submit,name="signup_submit"),
    url(r'^signup/result$', views.signup_result,name="signup_result"),
    url(r'^signup$', views.signup_index,name="signup_index"),
    url(r'^score/submit$', views.score_submit,name="score_submit"),
    url(r'^score/result$', views.score_result,name="score_result"),
    url(r'^score$', views.score_index,name="score_index"),
    url(r'^$', views.jpclass_index,name="jpclass_index"),
)
