from django.test import TestCase
from django.urls import reverse

from .models import Product


class HomePageTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')


class ProductTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title='test title',
            description='test product description',
            image='image.jpg',
            price=9.99,
            stock=1,
            slug='test-title',
        )

    def test_product(self):
        self.assertEqual(self.product.title, 'test title')
        self.assertEqual(self.product.description, 'test product description')
        self.assertEqual(self.product.slug, 'test-title')

    def test_product_list_view(self):
        response = self.client.get(reverse('product-list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test-title')
        self.assertTemplateUsed(response, 'products/product_list.html')