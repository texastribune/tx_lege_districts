from django.conf.urls.defaults import *

urlpatterns = patterns('lege_districts.views',
    url('^lookup/$', 'lookup', name='lege_districts_lookup'),
    url('^map/$', 'map', name='lege_districts_map'),
)
