# from urllib import request
# from django.http import request
import json

from django.views.generic import TemplateView, ListView
from rest_framework import generics, viewsets, permissions
# from urllib3.util import request

from rest_framework.response import Response

from order.serializers import *


class CartListAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    pass


from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# class IsOwner(permissions.BasePermission):
#
#     # def has_permission(self, request, view):
#     #     if obj.owner == request.user:
#     #      return True
#
#     def has_oject_permission(self, request, view, obj):
#         # orders = CartItem.objects.get(cart__costumer__user=request.user, cart__status='NPAY')
#         # if request.method in permissions.SAFE_METHODS:
#         #     return True
#         # elif obj in orders.cartitem_set:
#         #     return True
#         # else:
#         #     return False
#         if obj.owner.id == request.user.id:
#             return True
#
#
# class AddCartItemViewSet(viewsets.ModelViewSet):
#     serializer_class = CartItemSerializer
#     queryset = CartItem.objects.all()
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated, IsOwner]
#
#
# class forVIEWtemplate(TemplateView):
#     template_name = 'for_test.html'

class AddToCart(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            request.data._mutable = True
            # id_product = request.data['id_product']
            # count = request.data['count']
            user = request.user
            costumer = Costumer.objects.get_or_create(user=user)
            cart = Cart.objects.get_or_create(costumer=costumer[0], status='NPY')[0]
            request.data['cart'] = cart.id
            return super().create(request, *args, **kwargs)


#


class CartItemList(ListView):
    model = CartItem
    template_name = 'order/modalcart.html'
    context_object_name = 'items'

    def get_queryset(self):
        return CartItem.objects.filter(cart__costumer__user=self.request.user)

#
# def set_cart_cookie(request):
#     id_product = request.data['id_product']
#     count_product = int(request.data['count'])
#     product = request.COOKIES.get('product')
#     if product:
#         cok_dict = json.loads(product)
#         if id_product in cok_dict.keys():
#             cok_dict[id_product] = cok_dict[id_product] + count_product
#             return json.dumps(cok_dict)
#         cok_dict[id_product] = count_product
#         return json.dumps(cok_dict)
#     return json.dumps({id_product: count_product})
