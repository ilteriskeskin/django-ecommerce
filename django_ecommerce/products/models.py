from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Category Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Category Slug')
    ordering = models.IntegerField(default=1, verbose_name='Category Ordering')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Product Title')
    description = models.TextField(verbose_name='Product Description')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Product Price')
    image = models.ImageField(upload_to='media/', verbose_name='Product Image')
    stock = models.IntegerField(verbose_name='Product Stock')
    slug = models.SlugField(verbose_name='Product Slug', unique=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Product Date Added')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'category_slug': str(self.category.slug), 'slug': str(self.slug)})
