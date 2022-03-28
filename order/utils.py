import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from requests import Response

from order.models import CartItem


def set_cart_cookie(request):
    id_product = request.data['product']
    count_product = int(request.data['number_item'])
    product = request.COOKIES.get('cookie_product')
    # print('get', request.COOKIES.get('cookie_product'))
    if product:
        cok_dict = json.loads(product)
        if id_product in cok_dict.keys():
            cok_dict[id_product] = cok_dict[id_product] + count_product
            return json.dumps(cok_dict)
        cok_dict[id_product] = count_product
        return json.dumps(cok_dict)
    return json.dumps({id_product: count_product})


# utiles for set list of majazi order item
def list_of_cookie_to_cartItem(request):
    cookie_dict = request.COOKIES.get('cookie_product')
    print(cookie_dict)
    if cookie_dict == None:
        return 1
    json_cook = json.loads(cookie_dict)
    order_item_list = []
    for product_id, count in json_cook.items():
        cart_item = CartItem(product_id=int(product_id), number_item=count)
        order_item_list.append(cart_item)
    return order_item_list


def delete_item_in_cookie(request, pk):
    cookie_dict = request.COOKIES.get('cookie_product')
    json_cook = json.loads(cookie_dict)
    if pk in json_cook.keys():
        del json_cook[str(pk)]
        return json.dumps(json_cook)
