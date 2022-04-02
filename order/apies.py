import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import generics, viewsets, permissions
# from urllib3.util import request

from rest_framework.response import Response

from order.serializers import *
from order.utils import set_cart_cookie, list_of_cookie_to_cartItem, delete_item_in_cookie, update_item_in_cookie


class AddToCart(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    # def update(self, request, *args, **kwargs):
    #     if self.request.user.is_anonymous:
    #         product_id = self.request.data['product_id']
    #         count = self.request.data['count']
    #         # print(product_id)
    #         json_for_set_in_cookie = update_item_in_cookie(self.request, product_id, count)
    #         response = Response(status=201)
    #         response.set_cookie('cookie_product', json_for_set_in_cookie)
    #         return response
    #     else:
    #         print('inja count', self.request.data['count'])
    #         kwargs['partial'] = True
    #         print(kwargs['cart'])
    #         print(kwargs['number_item'])
    #         print(kwargs['product'])
    #         kwargs['number_item'] = self.request.data['count']
    #         return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            product_id = self.request.data['product']
            count = self.request.data['number_item']
            # print(product_id)
            json_for_set_in_cookie = update_item_in_cookie(self.request, product_id, count)
            response = Response(status=201)
            response.set_cookie('cookie_product', json_for_set_in_cookie)
            return response
        else:
            return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            product_id = self.request.data['product_id']
            # print(product_id)
            json_for_set_in_cookie = delete_item_in_cookie(self.request, product_id)
            response = Response(status=201)
            response.set_cookie('cookie_product', json_for_set_in_cookie)
            return response
        else:
            return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        product_id = self.request.data['product']
        if self.request.user.is_authenticated:
            try:
                # CartItem.objects.get(product_id=product_id, cart__costumer__user=self.request.user, cart__status='NPY')
                cart_item = CartItem.objects.get(product_id=product_id, cart__costumer__user=self.request.user,
                                                 cart__status='NPY')
                # print('show number item', cart_item.number_item)
                cart_item.number_item += 1
                cart_item.save()
                # print('2', cart_item.number_item)
                return HttpResponse('updated')
            except:
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
            try:
                cart = Cart.objects.get(costumer=costumer, status='NPY')
                print('count', cart.cartitem_set.all().count())
            except:
                return 1
            if cart.cartitem_set.all().count() == 0:
                return 1
            return cart.cartitem_set.all()
        elif self.request.user.is_anonymous:
            list_order_item = list_of_cookie_to_cartItem(self.request)
            # if list_order_item == 1:
            #     return render(self.request, template_name='404.html')
            # else:
            if list_order_item == []:
                return 1
            print('aaa', list_order_item)
            return list_order_item

    def get_context_data(self, *, object_list=None, **kwargs):
        total_price = 0
        if self.request.user.is_authenticated:
            for item in CartItem.objects.filter(cart__costumer__user=self.request.user, cart__status='NPY'):
                total_price += item.total_cartitem_price
            kwargs['total_price'] = total_price
            kwargs['final_price'] = total_price
            kwargs['address'] = Address.objects.filter(costumer__user=self.request.user)
        elif self.request.user.is_anonymous:
            list_order_item = list_of_cookie_to_cartItem(self.request)
            if not list_order_item == 1:
                print('ooo', list_order_item)
                for item in list_order_item:
                    total_price += item.total_cartitem_price
                kwargs['total_price'] = total_price
                kwargs['final_price'] = total_price

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
            off_code = self.request.data['off_code']
            my_off_code = OffCode.objects.get(code=off_code)
            ID_off_code = my_off_code.id
            request.data._mutable = True
            request.data['off_code'] = ID_off_code
            return super().partial_update(request, *args, **kwargs)

        except:
            # print('bazam dardesar')
            return Response(status=400)


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


class ToNextStepCart(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def partial_update(self, request, *args, **kwargs):
        request.data._mutable = True
        total_price_user = int(float(self.request.data['total_price']))
        final_price_user = int(float(self.request.data['final_price']))
        off_code_id = self.request.data['off_code']
        print(off_code_id, type(off_code_id))
        total_price_admin = 0
        for item in CartItem.objects.filter(cart__costumer__user=self.request.user, cart__status='NPY'):
            total_price_admin += item.total_cartitem_price

        if off_code_id:
            off_code_id = int(off_code_id)
            off_obj = OffCode.objects.filter(pk=off_code_id)[0]
            print('off_obj', off_obj)
            final_price_admin = off_obj.discounted_price(total_price_admin)
            print('final_user', final_price_user)
            print('final_admin', final_price_admin)
            print(final_price_user == final_price_admin)
            if final_price_user == final_price_admin:
                request.data['status'] = 'PAY'
                return super().partial_update(request, *args, **kwargs)
            else:
                return HttpResponse(status=401)
        else:
            print('total-ad', total_price_admin)
            print('total-us', total_price_user)
            print('total-us', final_price_user)
            print(total_price_admin == final_price_user)
            if total_price_admin == final_price_user:
                request.data['status'] = 'PAY'
                return super().partial_update(request, *args, **kwargs)
            else:
                return HttpResponse(status=402)
        # try:
        #     print('offId',off_code_id)
        #     off_obj = OffCode.objects.get(pk=off_code_id)
        #     discount_calc = off_obj.discounted_price(total_price_admin)
        #     final_price_admin = total_price_admin - discount_calc
        #     print('final_user', final_price_user)
        #     print('final_admin', final_price_admin)
        #     print(final_price_user == final_price_admin)
        #     if final_price_user == final_price_admin:
        #         request.data['status'] = 'PAY'
        #         return super().partial_update(request, *args, **kwargs)
        #     else:
        #         return HttpResponse(status=401)
        # except:
        #     print('total-ad', total_price_admin)
        #     print('total-us', total_price_user)
        #     print('total-us', final_price_user)
        #     print(total_price_admin == final_price_user)
        #     if total_price_admin == final_price_user:
        #         request.data['status'] = 'PAY'
        #         return super().partial_update(request, *args, **kwargs)
        #     else:
        #         return HttpResponse(status=402)
