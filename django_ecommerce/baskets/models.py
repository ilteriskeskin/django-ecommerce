from django.db import models
from django.conf import settings
from django.urls import reverse

from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

    @staticmethod
    def get_absolute_url():
        return reverse('basket-detail')
