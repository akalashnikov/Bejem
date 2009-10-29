from django.conf.urls.defaults import *
#from users.views import index
import users.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^index/$', ...),
    #(r'^registration/$', ...),
    (r'^users/$', users.views.index),
    #(r'^users/[A-Za-z]+$', users.views.details),
    (r'^admin/$', include(admin.site.urls)),
    (r'^admin/doc/$', include('django.contrib.admindocs.urls')),
)
