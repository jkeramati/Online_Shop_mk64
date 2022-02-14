from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from order.models import Cart, CartItem


class CartListView(ListView):
    model = Cart
    template_name = ''


class CartItemListView(ListView):
    model = CartItem
    template_name = ''
