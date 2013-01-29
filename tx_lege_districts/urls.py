from django.conf.urls.defaults import *

urlpatterns = patterns('tx_lege_districts.views',
    url('^by-number/$', 'by_number', name='tx_lege_districts_by_number'),
    url('^lookup/$', 'lookup', name='tx_lege_districts_lookup'),
    url('^map/$', 'map', name='tx_lege_districts_map'),
)
