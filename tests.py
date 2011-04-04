from django.test import TestCase
from django.db import connections
from django.core.management import call_command

from districts.models import District, HOUSE, SENATE

class ModelTest(TestCase):
    multi_db = True
    fixtures = ['districts_2006']

    def test_unicode(self):
        district = District(number=1, type=HOUSE)
        self.assertEqual(u'House District 1', unicode(district))

    def test_save_not_implemented(self):
        district = District(number=1, type=HOUSE)
        self.assertRaises(NotImplementedError, district.save)

    def test_count(self):
        self.assertEqual(District.objects.count(), 181)

    def test_austin(self):
        austin_districts = District.objects.filter_by_lat_lng(30.3037, -97.7696)
        self.assertEqual(austin_districts.count(), 2)
        self.assertEqual(austin_districts.get(type=SENATE).number, 14)
        self.assertEqual(austin_districts.get(type=HOUSE).number, 48)
