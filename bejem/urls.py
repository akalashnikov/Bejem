import os

from django.conf.urls.defaults import *
from django.contrib import admin

import settings
import users.views

#css: is it right?
media = settings.rel('media')

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', users.views.index),
    (r'^registration/$', users.views.registration),
    (r'^login/$', users.views.login),
    (r'^logout/$', users.views.logout),
    (r'^users/$', users.views.user_list),
    (r'^users/[A-Za-z_]+$', users.views.user_list),
    (r'^search/$', users.views.search),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': media }),
)
 
