from django.contrib import admin

# Register your models here.
from short_link.models import Links, LinkStats


@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):
    pass

@admin.register(LinkStats)
class LinkStatsAdmin(admin.ModelAdmin):
    pass
