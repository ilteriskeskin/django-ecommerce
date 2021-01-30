from django.contrib import admin

from .models import Product, Category


class ProductInLine(admin.TabularInline):
    model = Product
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'stock',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInLine, ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
