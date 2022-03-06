# from urllib import request
# from django.http import request
from rest_framework import generics
# from urllib3.util import request

from order.serializers import *


class CartListAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartItemListAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
