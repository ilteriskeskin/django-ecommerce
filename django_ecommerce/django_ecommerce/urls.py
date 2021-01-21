from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

from products.views import SearchResultView
from products.models import Product


info_dict = {
    'queryset': Product.objects.all(),
}


urlpatterns = [
    # Default
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),

    # Products
    path('products/', include('products.urls')),

    # Basket
    path('basket/', include('baskets.urls')),

    # Searching
    path('search/', SearchResultView.as_view(), name='search'),

    # Sitemap
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6, protocol='https'), }},
         name='django.contrib.sitemaps.views.sitemap'),

    # Authentication
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
