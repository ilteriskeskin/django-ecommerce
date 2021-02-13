from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from products.views import SearchResultView
from products.models import Product


info_dict = {
    "queryset": Product.objects.all(),
}


urlpatterns = [
    # Default
    path("home/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    # Authentication
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    # Searching
    path("search/", SearchResultView.as_view(), name="search"),
    # Basket
    path("basket/", include("baskets.urls")),
    # Products
    path("", include("products.urls")),
    # Sitemap
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": {
                "blog": GenericSitemap(info_dict, priority=0.6, protocol="https"),
            }
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
