from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_create.html'
    fields = '__all__'
    login_url = 'login'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    fields = '__all__'
    login_url = 'login'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('product-list')  # After the action is successful, redirect to the desired page.


class SearchResultView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(title__icontains=query) # Searching for the field. In this case, Title
        # field.
        return object_list
