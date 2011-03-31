from django.test import TestCase
from django.db import connections

from districts.models import District, HOUSE, SENATE

class ModelTest(TestCase):
    def setUp(self):
        cursor = connections['districts'].cursor()
        cursor.execute("DROP TABLE districts_district")
        sql = open('districts/fixtures/districts.sql').read()
        for statement in sql.split(';\n'):
            cursor.execute(statement)

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
