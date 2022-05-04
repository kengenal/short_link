from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from short_link.api.views import ShortLinkGenerateApiView

from short_link.views import RedirectView

router = DefaultRouter()
router.register(
    'generate',
    ShortLinkGenerateApiView,
    basename="short-link-generator"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(
        '<slug:new_url>',
        RedirectView.as_view(),
        name='redirect-view'
    )
]
