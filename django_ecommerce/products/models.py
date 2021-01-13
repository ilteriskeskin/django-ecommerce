from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='media/',)
    stock = models.IntegerField()
    #category = models.ForeignKey()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': str(self.pk)})