from django.conf.urls import patterns, url, include

urlpatterns = patterns('tx_lege_districts.views',
    url('^by-number/$', 'by_number', name='by_number'),
    url('^lookup/$', 'lookup', name='lookup'),
    url('^map/$', 'map', name='map'),
    url('^api/', include(patterns('tx_lege_districts.views',
        url('^district/(?P<type>\w+)/(?P<number>\d+)/$', 'district_detail',
                name='district_detail'),
    ), namespace='api')),
)
