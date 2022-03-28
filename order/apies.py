import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import generics, viewsets, permissions
# from urllib3.util import request

from rest_framework.response import Response

from order.serializers import *
from order.utils import set_cart_cookie, list_of_cookie_to_cartItem


class AddToCart(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)

    def create(self, request, *args, **kwargs):
        product_id = self.request.data['product']
        if self.request.user.is_authenticated:
            if CartItem.objects.get(product_id=product_id, cart__costumer__user=self.request.user, cart__status='NPY'):
                cart_item = CartItem.objects.get(product_id=product_id, cart__costumer__user=self.request.user,
                                                 cart__status='NPY')
                print('show number item', cart_item.number_item)
                cart_item.number_item += 1
                cart_item.save()
                print('2', cart_item.number_item)
                return HttpResponse('updated')
            else:
                print(self.request.user)
                request.data._mutable = True
                # id_product = request.data['id_product']
                # count = request.data['count']
                user = request.user
                costumer = Costumer.objects.get_or_create(user=user)
                cart = Cart.objects.get_or_create(costumer=costumer[0], status='NPY')[0]
                request.data['cart'] = cart.id
                return super().create(request, *args, **kwargs)
        elif self.request.user.is_anonymous:
            cookie = set_cart_cookie(request)
            # print('cookiee:', cookie)
            response = Response(status=201)
            response.set_cookie('cookie_product', cookie)
            # print('get', request.COOKIES.get('cookie_product'))
            # print('response', response)
            return response


class CartItemList(ListView):
    model = CartItem
    template_name = 'order/samplecart.html'
    context_object_name = 'items'

    def get_queryset(self):
        # cookie = self.request.COOKIES.get('cookie_product')
        if self.request.user.is_authenticated:
            user = self.request.user
            costumer = Costumer.objects.get(user=user)
            cart = Cart.objects.get(costumer=costumer, status='NPY')
            return cart.cartitem_set.all()
        elif self.request.user.is_anonymous:
            list_order_item = list_of_cookie_to_cartItem(self.request)
            # if list_order_item == 1:
            #     return render(self.request, template_name='404.html')
            # else:
            return list_order_item

    def get_context_data(self, *, object_list=None, **kwargs):
        total_price = 0
        if self.request.user.is_authenticated:
            for item in CartItem.objects.filter(cart__costumer__user=self.request.user):
                total_price += item.product.price * item.number_item
            kwargs['total_price'] = total_price
            kwargs['tax'] = total_price * 0.05
            kwargs['final_price'] = total_price + total_price * 0.05
        elif self.request.user.is_anonymous:
            pass
            # for item in CartItem.objects.get():
            #     total_price += item.product.price * item.number_item
            # kwargs['total_price'] = total_price
            # kwargs['tax'] = total_price * 0.05
            # kwargs['final_price'] = total_price + total_price * 0.05

        return super().get_context_data(object_list=object_list, **kwargs)


class CartItemListCookie(ListView):
    model = CartItem
    template_name = 'order/cart_for_cookie.html'
    context_object_name = 'items'

    def get_queryset(self):
        cookie = self.request.COOKIES.get('cookie_product')
        print('cookie for test', cookie)
        return super().get_queryset()


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

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            print('yesssssaaa')
        return super().destroy(request, *args, **kwargs)


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
