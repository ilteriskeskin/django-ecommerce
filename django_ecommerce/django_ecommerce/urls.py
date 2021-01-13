from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from products import views as ProductViews


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),

    # Authentication.
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

    # Products.
    path('products/', include('products.urls')),

    # Searching.
    path('search/', ProductViews.SearchResultView.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)