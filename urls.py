from django.conf.urls.defaults import *

urlpatterns = patterns('districts.views',
    url('^lookup/$', 'lookup', name='districts_lookup'),
)