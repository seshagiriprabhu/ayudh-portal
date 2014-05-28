from django.conf.urls import *
#from inctf.register import views
from ayudh import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',views.home),
    (r'^register',include('register.urls')),
    (r'^login/$',views.login),
    (r'^logout/$',views.logout),
    (r'^about/$',views.about),
)
