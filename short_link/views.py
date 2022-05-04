from django.shortcuts import HttpResponseRedirect
from django.views.generic import DetailView

from short_link.models import Links, LinkStats


class RedirectView(DetailView):
    model = Links
    stats_model = LinkStats
    slug_url_kwarg = 'new_url'
    slug_field = 'new_url'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.stats()
        return HttpResponseRedirect(redirect_to=self.object.url)

    def stats(self):
        self.stats_model.objects.create(
            ip=self.request.META.get("REMOTE_ADDR"),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            link=self.object
        )
