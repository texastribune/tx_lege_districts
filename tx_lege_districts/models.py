from django.contrib.gis.db import models

HOUSE = 'HOUSE'
SENATE = 'SENATE'

DISTRICT_TYPES = (
    (HOUSE, 'House'),
    (SENATE, 'Senate'),
)

REMEDIAL = 'REMEDIAL'
INTERIM = 'INTERIM'
FINAL = 'FINAL'
STATUSES = (
    (REMEDIAL, 'Remedial'),
    (INTERIM, 'Interim'),
    (FINAL, 'Final')
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
    status = models.CharField(max_length=100, choices=STATUSES)
    number = models.IntegerField()
    year = models.IntegerField()
    geometry = models.MultiPolygonField()

    def __unicode__(self):
        return u'%s District %d' % (self.get_type_display(), self.number)

    class Meta:
        unique_together = ('type', 'number', 'year')
        ordering = ('type', 'number')
