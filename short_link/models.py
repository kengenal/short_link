from django.db import models

class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Links(DateModel):
    new_url = models.CharField(
        max_length=120,
        unique=True,
        blank=True,
        null=True
    )
    url = models.URLField(
        unique=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.new_url)

class LinkStats(DateModel):
    link = models.ForeignKey("Links", on_delete=models.CASCADE)
    ip = models.CharField(max_length=120)
    user_agent = models.CharField(max_length=120)

    def __str__(self):
        return str(self.link.new_url)
