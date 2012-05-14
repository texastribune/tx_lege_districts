from django.contrib.gis import admin
from models import District


class DistrictAdmin(admin.GeoModelAdmin):
    list_display = ('__unicode__', 'year')
    list_filter = ('type', 'year')

admin.site.register(District, DistrictAdmin)
