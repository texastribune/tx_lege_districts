import json

from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from .models import District
from .constants import HOUSE, SENATE, INTERIM

DUMMY_DISTRICT_NUMBER = 201
DUMMY_REPRESENTATIVE = 'Test Representative'


class DummyBackend(object):
    def get_representative(self, district):
        if district.number == DUMMY_DISTRICT_NUMBER:
            return DUMMY_REPRESENTATIVE


class TestDistricts(TestCase):
    multi_db = True
    fixtures = ['districts_2006']

    def test_unicode(self):
        district = District(number=1, type=HOUSE)
        self.assertEqual(u'House District 1', unicode(district))

    def test_count(self):
        self.assertEqual(District.objects.count(), 181)

    def test_austin(self):
        austin_districts = District.objects.filter_by_lat_lng(30.3037, -97.7696)
        self.assertEqual(austin_districts.count(), 2)
        self.assertEqual(austin_districts.get(type=SENATE).number, 14)
        self.assertEqual(austin_districts.get(type=HOUSE).number, 48)

    def test_unique_constraint(self):
        district = District.objects.get(number=1, type=HOUSE, year=2006)
        District.objects.create(number=1, type=HOUSE, year=2012, status=INTERIM,
                                geometry=district.geometry)
        qs = District.objects.filter(number=1, type=HOUSE)
        self.assertEqual(qs.count(), 2)

    def test_lookup(self):
        url = reverse('tx_lege_districts_lookup')

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


class TestBackends(TestCase):
    key = 'TX_REPRESENTATIVE_BACKENDS'
    dummy_backends = ['tx_lege_districts.tests.DummyBackend']
    district = District(number=DUMMY_DISTRICT_NUMBER)

    def setUp(self):
        if hasattr(settings, self.key):
            self.original_backends = getattr(settings, self.key)
            delattr(settings, self.key)

    def tearDown(self):
        if hasattr(self, 'original_backends'):
            setattr(settings, self.key, self.original_backends)

    def test_get_representative_returns_none_by_default(self):
        self.assertEqual(self.district.representative, None)

    def test_get_representative_with_simple_backend(self):
        setattr(settings, self.key, self.dummy_backends)
        self.assertEqual(self.district.representative, DUMMY_REPRESENTATIVE)
