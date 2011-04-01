from django.contrib.gis import admin
from models import District

admin.site.register(District, admin.GeoModelAdmin)