from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import viewsets

from order.models import Cart, CartItem


class CartListView(ListView):
    model = Cart
    template_name = 'order/cart_item.html'


class CartItemListView(ListView):
    model = CartItem
    template_name = ''






