from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryDetailView
)


urlpatterns = [
    # Product list & detail
    path('', ProductListView.as_view(), name='product-list'),
    path('<slug:category_slug>/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),

    # Category Detail
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),

    # CRUD
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
