from django.urls import reverse
from rest_framework import serializers

from short_link.models import Links


class ShortLinkSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField(read_only=True)
    url = serializers.URLField(required=True)
    stats = serializers.IntegerField(source='linkstats_set.count', read_only=True)

    class Meta:
        model = Links
        read_only_fields = ['new_url', 'stats', 'link']
        fields = ['url'] + read_only_fields

    def get_link(self, obj):
        return self.context.get(
            'request'
        ).build_absolute_uri(
            reverse('redirect-view', kwargs={'new_url': obj.new_url})
        )

    def create(self, validated_data):
        model = self.Meta.model.objects.filter(url=validated_data.get('url'))
        if model.exists():
            return model.first()
        return super().create(validated_data)
