import json

from order.models import CartItem, Cart
from product.models import Product


def count_basket(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(costumer__user=request.user, status='NPY')
        print('cart:', cart)
        try:
            cart_item = CartItem.objects.filter(cart=cart[0])
        except:
            return {
                'number_basket': 0
            }
        print('cart_item:', cart_item)
        count = 0
        for item in cart_item:
            count += item.number_item
        return {
            'number_basket': count
        }
    elif request.user.is_anonymous:
        cookie_dict = request.COOKIES.get('cookie_product')
        try:
            json_cook = json.loads(cookie_dict)
            count = 0
            for item in json_cook.values():
                count += item
            return {
                'number_basket': count
            }
        except:
            return {
                'number_basket': 0
            }
