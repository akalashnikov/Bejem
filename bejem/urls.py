import os

from django.conf.urls.defaults import *
from django.contrib import admin

#from registration import views

import settings
import users.views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', users.views.index),
    (r'^registration/$', users.views.registration),
    (r'^login/$', users.views.login),
    (r'^logout/$', users.views.logout),
    (r'^users/$', users.views.user_list),
    (r'^users/[A-Za-z0-9_]+$', users.views.user_list),
    (r'^search/$', users.views.search),
    (r'^secret/$', users.views.secret),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/', include('registration.urls')),
)

#    url(r'/register', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
#    url('', include('registration.urls')),

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
