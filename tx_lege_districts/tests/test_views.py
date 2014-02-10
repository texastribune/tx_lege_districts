from django.test import TestCase
from django.test.client import RequestFactory

from ..views import JsonpResponse


class JsonpResponseTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_returns_json(self):
        request = self.factory.get('')
        response = JsonpResponse('content', request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_returns_jsonp_with_callback(self):
        request = self.factory.get('', {'callback': 'poop'})
        response = JsonpResponse('content', request)
        self.assertEqual(response.status_code, 200)
        # content type should be different than before
        self.assertEqual(response['Content-Type'], 'application/javascript')
        # callback should wrap content
        self.assertEqual(response.content, 'poop(content)')
