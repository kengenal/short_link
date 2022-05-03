from rest_framework.test import APITestCase, APIRequestFactory


class TestStatsLinkViews(APITestCase):
    def setUp(self):
        self.client = APIRequestFactory()
