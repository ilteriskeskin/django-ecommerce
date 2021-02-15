from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Order


@login_required()
def basket_view(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {
        "items": items,
        "order": order,
    }

    return render(request, "basket/basket.html", context)
