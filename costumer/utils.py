import json

from costumer.models import Costumer
from order.models import CartItem, Cart


def send_cartItem_cookie_to_DB(request):
    cookie_dict = request.COOKIES.get('cookie_product')
    json_cook = json.loads(cookie_dict)
    user = request.user
    costumer = Costumer.objects.get_or_create(user=user)
    # print('costid', costumer.id)
    cart = Cart.objects.get_or_create(costumer=costumer[0], status='NPY')
    for product_id, count in json_cook.items():
        CartItem.objects.create(cart=cart[0], product_id=product_id, number_item=count)
