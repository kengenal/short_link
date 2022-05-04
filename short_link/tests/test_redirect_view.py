from django.conf import settings
from django.test import TestCase, Client
from django.utils.crypto import get_random_string
from rest_framework import status

from short_link.models import Links


class TestRedirectView(TestCase):
    def setUp(self):
        self.client = Client()
        self.DOMAIN = "http://google.com"

    def test_redirect_with_existing_url(self):
        """ Should be redirected to correct website """

        obj = Links.objects.create(
            url=self.DOMAIN,
            new_url=get_random_string(settings.SHORT_LINK_LENGTH)
        )
        request = self.client.get(f"/{obj.new_url}")

        self.assertEqual(request.status_code, status.HTTP_302_FOUND)
        self.assertEqual(request.headers.get('Location'), obj.url)

    def test_redirect_url_not_exists(self):

        request = self.client.get('/test/')

        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
