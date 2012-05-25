from armstrong.utils.backends import GenericBackend, DID_NOT_HANDLE
from django.contrib.gis.db import models
from django.core.exceptions import ImproperlyConfigured

from .constants import TYPE_CHOICES, STATUS_CHOICES

# A generic backend that defines a method `get_representative(self, district)`
representative_backend = GenericBackend("TX_REPRESENTATIVE_BACKENDS")


class DistrictManager(models.GeoManager):
    def filter_by_lat_lng(self, lat, lng):
        point_text = "POINT(%f %f)" % (lng, lat)
        return self.get_query_set().filter(geometry__contains=point_text)


class District(models.Model):
    """
    A legislative district in the State of Texas.
    """
    objects = DistrictManager()

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    number = models.IntegerField()
    year = models.IntegerField()
    geometry = models.MultiPolygonField()

    def __unicode__(self):
        return u'%s District %d' % (self.get_type_display(), self.number)

    class Meta:
        unique_together = ('type', 'number', 'year')
        ordering = ('type', 'number')

    @property
    def representative(self):
        try:
            backend = representative_backend.get_backend()
            return backend.get_representative(self)
        except (ImproperlyConfigured, DID_NOT_HANDLE):
            return None
