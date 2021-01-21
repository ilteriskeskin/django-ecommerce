from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from .models import Basket


class BasketDetailView(LoginRequiredMixin, DetailView):
    model = Basket
    context_object_name = 'basket_list'
    template_name = 'basket/basket_list.html'

    def get(self, request, *args, **kwargs):
        basket = Basket.objects.filter(user=request.user, ordered=False)

        if basket:
            return render(request, "basket/basket_list.html")

        return render(request, "home.html")
