from django.conf import settings
from django.test import TestCase, Client
from django.utils.crypto import get_random_string
from rest_framework import status

from short_link.models import Links, LinkStats


class BestShortLinkTestCase(TestCase):
    def setUp(self):
        self.client = Client(
            HTTP_USER_AGENT='Mozilla/5.0',
            REMOTE_ADDR='127.0.0.1'
        )
        self.DOMAIN = "http://google.com"
        self.obj = Links.objects.create(
            url=self.DOMAIN,
            new_url=get_random_string(settings.SHORT_LINK_LENGTH)
        )


class TestRedirectView(BestShortLinkTestCase):
    def test_redirect_with_existing_url(self):
        """ Should be redirected to correct website """

        request = self.client.get(f"/{self.obj.new_url}")

        self.assertEqual(request.status_code, status.HTTP_302_FOUND)
        self.assertEqual(request.headers.get('Location'), self.obj.url)

    def test_redirect_url_not_exists(self):
        request = self.client.get('/test/')

        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)


class TestShortLinkStats(BestShortLinkTestCase):
    def test_stats_for_existing_url(self):
        """ should be redirected and add record to the Stats """

        self.client.get(f"/{self.obj.new_url}")

        stats = LinkStats.objects.all()

        self.assertEqual(stats.count(), 1)
        self.assertEqual(stats.first().link, self.obj)

    def test_stats_multiple_requests(self):
        """ Should be created multiple record in database for one link """
        counter = 3
        for _ in range(counter):
            self.client.get(f"/{self.obj.new_url}")

        stats = LinkStats.objects.all()

        self.assertEqual(stats.count(), counter)
        self.assertEqual(stats.first().link, self.obj)

    def test_stats_but_url_not_exists(self):
        """ Should be not add to stats model"""

        self.client.get("random")
        stats = LinkStats.objects.all()

        self.assertEqual(stats.count(), 0)

