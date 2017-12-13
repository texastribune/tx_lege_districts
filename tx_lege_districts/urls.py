from django.conf.urls import url, include

from tx_lege_districts import views

app_name = 'tx_lege_districts'

urlpatterns = [
    url('^by-number/$', views.by_number, name='by_number'),
    url('^lookup/$', views.lookup, name='lookup'),
    url('^map/$', views.map, name='map'),
    url('^api/', include([
                        url('^district/(?P<type>\w+)/(?P<number>\d+)/$',
                            views.district_detail,
                            name='district_detail'),
                    ])
        ),
]
