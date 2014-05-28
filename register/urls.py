from django.conf.urls import *
from register import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^/$',views.register),
    (r'^/user/$',views.registeruser),
    (r'^/user/success/$',views.userregistrationsuccess),
    (r'^/userregvisual/$', views.visualreg),
)
