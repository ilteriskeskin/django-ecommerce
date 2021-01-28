from django.views.generic import ListView, DetailView

from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class SearchResultView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(title__icontains=query)  # Searching for the field. In this case, Title
        # field.
        return object_list


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'
