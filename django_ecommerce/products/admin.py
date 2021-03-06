from django.contrib import admin

from .models import Product, Category


class ProductInLine(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "price",
        "stock",
        "date_added",
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    list_filter = ("category",)
    date_hierarchy = "date_added"
    order_by = "-date_added"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]
    prepopulated_fields = {"slug": ("title",)}
