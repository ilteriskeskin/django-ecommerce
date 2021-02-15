from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryDetailView, basket_view


urlpatterns = [
    # Product list & detail
    path("", ProductListView.as_view(), name="product-list"),
    path(
        "<slug:category_slug>/<slug:slug>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
    # Basket
    path("basket/", basket_view, name="basket"),
    # Category Detail
    path("<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
]
