from django.urls import path
from .views import basket_detail


urlpatterns = [
    path("", basket_detail, name="basket-detail"),
]
