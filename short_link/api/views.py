from django.conf import settings
from django.utils.crypto import get_random_string

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from short_link.api.serializers import ShortLinkSerializer
from short_link.models import Links


class ShortLinkGenerateApiView(CreateModelMixin, GenericViewSet):
    serializer_class = ShortLinkSerializer
    queryset = Links.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            new_url=get_random_string(
                settings.SHORT_LINK_LENGTH
            )
        )
