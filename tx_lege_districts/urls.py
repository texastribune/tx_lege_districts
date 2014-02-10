from django.conf.urls import patterns, url

urlpatterns = patterns('tx_lege_districts.views',
    url('^by-number/$', 'by_number', name='by_number'),
    url('^lookup/$', 'lookup', name='lookup'),
    url('^map/$', 'map', name='map'),
)
