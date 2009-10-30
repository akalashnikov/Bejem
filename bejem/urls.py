from django.conf.urls.defaults import *
from django.contrib import admin
#from users.views import index
import users.views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', users.views.index),
    (r'^registration/$', users.views.registration),
    (r'^login/$', users.views.login),
    (r'^users/$', users.views.user_list),
    (r'^users/[A-Za-z]+$', users.views.user_list),
    (r'^search/$', users.views.search),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
 
