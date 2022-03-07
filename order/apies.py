# from urllib import request
# from django.http import request
from rest_framework import generics, viewsets
# from urllib3.util import request

from order.serializers import *


class CartListAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()





class CartItemListAPI(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def cookie_response(self, request):
        product = Product.objects.get(id=request.data['id_product'])

