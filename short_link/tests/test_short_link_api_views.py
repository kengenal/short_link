from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from short_link.api.serializers import ShortLinkSerializer
from short_link.models import Links


class TestShortLinkGenerateViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.URL = '/api/generate/'
        self.METHOD_NOT_ALLOWED = ('GET', 'PUT', 'PATCH', 'HEAD')
        self.DOMAIN = "http://google.com"

    def test_methods_not_allowed(self):
        for method in self.METHOD_NOT_ALLOWED:
            request = self.client.generic(method, self.URL)
            self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_generate_new_link_link_not_existing_in_database(self):
        """ Should be created new record in database and return short link """
        request = self.client.post(self.URL, {"url": self.DOMAIN})

        obj = Links.objects.get(url=self.DOMAIN)

        self.assertEqual(Links.objects.all().count(), 1)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.data, ShortLinkSerializer(
            obj, context={'request': request.wsgi_request}
        ).data)
        self.assertIsNotNone(request.data['link'])

    def test_generate_link_but_link_exists_in_database(self):
        """ Should be return link without create """

        obj = Links.objects.create(url=self.DOMAIN)
        request = self.client.post(self.URL, {'url': self.DOMAIN})

        obj.refresh_from_db()

        self.assertEqual(Links.objects.all().count(), 1)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.data, ShortLinkSerializer(
            obj, context={'request': request.wsgi_request}
        ).data)

    def test_generate_user_provide_wrong_url_address(self):
        """ Should be return 400 with error message"""
        request = self.client.post(self.URL, {"url": "wrong"})

        self.assertEqual(request.data['url'][0], 'Enter a valid URL.')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)


    def test_generate_but_url_is_none(self):
        """ Should be return error code 400 with error message """
        request = self.client.post(self.URL, {})

        self.assertEqual(request.data['url'][0], 'This field is required.')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
