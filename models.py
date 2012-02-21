from django.contrib.gis.db import models
from django.db.models.signals import post_syncdb

HOUSE = 'HOUSE'
SENATE = 'SENATE'

DISTRICT_TYPES = (
    (HOUSE, 'House'),
    (SENATE, 'Senate'),
)

class DistrictManager(models.GeoManager):
    def filter_by_lat_lng(self, lat, lng):
        point_text = "POINT(%f %f)" % (lng, lat)
        return self.get_query_set().filter(geometry__contains=point_text)


class District(models.Model):
    """
    This is a geographic model, but the Geometry is should only be queried
    inside spatialite in order to avoid all the dependencies of a full
    GeoDjango setup
    """
    objects = DistrictManager()
    
    type = models.CharField(max_length=100, choices=DISTRICT_TYPES)
    number = models.IntegerField()
    year = models.IntegerField()
    geometry = models.MultiPolygonField()

    def __unicode__(self):
        return u'%s District %d' % (self.get_type_display(), self.number)

    class Meta:
        unique_together = ('type', 'number')
        ordering = ('type', 'number')

    def save(self, *args, **kwargs):
        raise NotImplementedError, \
            'Districts should only be loaded from shapefiles'
