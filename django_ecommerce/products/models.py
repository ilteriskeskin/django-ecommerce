from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Product Title')
    description = models.TextField(verbose_name='Product Description')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Product Price')
    image = models.ImageField(upload_to='media/', verbose_name='Product Image')
    stock = models.IntegerField(verbose_name='Product Stock')
    slug = models.SlugField(verbose_name='Product Slug')
    # category = models.ForeignKey()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': str(self.pk)})