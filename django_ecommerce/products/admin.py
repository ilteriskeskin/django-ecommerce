from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'stock',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
