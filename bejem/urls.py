import os

from django.conf.urls.defaults import *
from django.contrib import admin

import settings
import users.views

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
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.rel('media') }),
    )

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#    )
