from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string

class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Links(DateModel):
    link_id = models.CharField(
        max_length=120,
        unique=True,
        default=get_random_string(settings.SHORT_LINK_LENGTH),
        blank=True,
        null=True
    )
    main_url = models.URLField()

    def __str__(self):
        return str(self.link_id)

class LinkStats(DateModel):
    link = models.ForeignKey("Links", on_delete=models.CASCADE)
    ip = models.CharField(max_length=120)
    user_agent = models.CharField(max_length=120)

    def __str__(self):
        return str(self.link.link_id)
