from django.urls import path
from .views import BasketDetailView


urlpatterns = [
    path("", BasketDetailView.as_view(), name="basket-detail"),
]
