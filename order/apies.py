from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import generics, viewsets, permissions
# from urllib3.util import request

from rest_framework.response import Response

from order.serializers import *


class AddToCart(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

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


class CartItemList(ListView):
    model = CartItem
    template_name = 'order/samplecart.html'
    context_object_name = 'items'

    def get_queryset(self):
        return CartItem.objects.filter(cart__costumer__user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        total_price = 0
        for item in CartItem.objects.filter(cart__costumer__user=self.request.user):
            total_price += item.product.price * item.number_item
        kwargs['total_price'] = total_price
        kwargs['tax'] = total_price * 0.05
        kwargs['final_price'] = total_price + total_price * 0.05

        return super().get_context_data(object_list=object_list, **kwargs)


def samplecart(requset):
    return render(requset, 'order/modalcart.html')


class CartUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def partial_update(self, request, *args, **kwargs):
        try:
            off_code = request.data['off_code']
            id_off_code = OffCode.objects.get(code=off_code)
            print(id_off_code)
        except:
            print('bazam dardesar')
            return Response(status=404)

        return super().partial_update(request, *args, **kwargs)


class CartItemDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem


class CartItemListApi(generics.ListAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        # print(self.request.GET['cart_id'])
        queryset = CartItem.objects.filter(cart_id=self.request.GET['cart_id'])
        # print(queryset)
        return queryset

    # def get_queryset(self):
    #     cart_id = self.request.data['cart_id']
    #     queryset = CartItem.objects.filter(cart_id=cart_id)
    #     return queryset

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
