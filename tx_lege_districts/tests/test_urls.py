import json

from django.core.urlresolvers import reverse
from django.test import TestCase


class URLTests(TestCase):
    fixtures = ['districts_2006']

    def test_tx_lege_districts_by_number(self):
        url = reverse('tx_lege_districts_by_number')
        url += '?type=house&number=1&number=2'  # too lazy to %s
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tx_lege_districts_by_number_returns_402_with_no_data(self):
        url = reverse('tx_lege_districts_by_number')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 402)

    def test_tx_lege_districts_lookup(self):
        url = reverse('tx_lege_districts_lookup')
        response = self.client.get(url, {'lat': '30', 'lng': '-100'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data)

    def test_tx_lege_districts_lookup_returns_empty_with_no_data(self):
        url = reverse('tx_lege_districts_lookup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{}')

    def test_tx_lege_districts_map(self):
        url = reverse('tx_lege_districts_map')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
