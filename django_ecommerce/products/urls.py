from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryDetailView


urlpatterns = [
    # Product list & detail
    path("", ProductListView.as_view(), name="product-list"),
    path(
        "<slug:category_slug>/<slug:slug>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
    # Category Detail
    path("<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
]
