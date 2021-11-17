from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from orders.forms import OrderModelForm
from orders.models import OrderModel
from products.models import ProductModel


class OrderCreateView(CreateView):
    template_name = 'checkout2.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('orders:history')

    def dispatch(self, request, *args, **kwargs):
        if len(request.session.get('cart', [])) == 0:
            return redirect(reverse('contact:home'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.get_from_cart(self.request)
        return context

    def form_valid(self, form):
        products = ProductModel.get_from_cart(self.request)
        price = products.aggregate(Sum('real_price')).get('real_price__sum', 0)

        form.instance.price = price
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user

        order = form.save()
        order.products.set(products)
        order.save()

        self.request.session['cart'] = []

        return redirect(self.get_success_url())


class OrderHistoryListView(LoginRequiredMixin, ListView):
    template_name = 'history.html'

    def get_queryset(self):
        return OrderModel.objects.filter()
