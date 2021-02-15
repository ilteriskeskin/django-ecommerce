from django.urls import path

from .views import basket_view, checkout_view


urlpatterns = [
    path("basket/", basket_view, name="basket"),
    path("checkout/", checkout_view, name="checkout"),
]
