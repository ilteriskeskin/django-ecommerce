from django.contrib import admin

from .models import Order, OrderItem, Customer


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "order",
        "quantity",
        "date_added",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInLine,
    ]
    list_display = (
        "customer",
        "date_ordered",
        "transaction_id",
    )


admin.site.register(Customer)
