from django.shortcuts import HttpResponseRedirect
from django.views.generic import DetailView

from short_link.models import Links


class RedirectView(DetailView):
    model = Links
    slug_url_kwarg = 'new_url'
    slug_field = 'new_url'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to=self.object.url)
