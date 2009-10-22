from django.conf.urls.defaults import *
from users.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^users/', index),
    (r'^admin/', include(admin.site.urls)),
    (r'^admon/doc/', include('django.contrib.admindocs.urls')),
)
