from rest_framework.test import APITestCase, APIRequestFactory


class TestShortLinkViews(APITestCase):
    def setUp(self):
        self.client = APIRequestFactory()
