import json

from django.core.urlresolvers import reverse
from django.test import TestCase


class URLTests(TestCase):
    fixtures = ['districts_2006']

    def test_by_number(self):
        url = reverse('tx_lege_districts:by_number')
        url += '?type=house&number=1&number=2'  # too lazy to %s
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_by_number_returns_402_with_no_data(self):
        url = reverse('tx_lege_districts:by_number')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 402)

    def test_lookup(self):
        url = reverse('tx_lege_districts:lookup')

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

    def test_map(self):
        url = reverse('tx_lege_districts:map')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
