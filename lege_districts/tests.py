import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from districts.models import District, HOUSE, SENATE


class DistrictsTest(TestCase):
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

    def test_lookup(self):
        url = reverse('districts_lookup')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data, {})

        response = self.client.get(url, {'lat': '30.3037', 'lng': '-97.7696'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['senate']['number'], 14)
        self.assertEqual(data['house']['number'], 48)
        self.assertEqual('coordinates' in data['senate'], True)
        self.assertEqual('coordinates' in data['house'], True)
