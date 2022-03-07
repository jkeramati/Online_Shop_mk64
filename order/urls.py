from django.urls import path, include

# from order.context import number_order_cart
# from order.utils import set_cookie
from order.views import CartListView, CartItemListView, modal_cart

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart_list_view'),
    path('cartitem/', CartItemListView.as_view(), name='cartitem_list_view'),
    path('cart/', modal_cart, name='modal_cart'),
    path('modal/', modal_cart, name='modal_cart'),
    # path('add_cart/', number_order_cart, name='add_cart'),
    # path('set_cookie/', set_cookie, name='set_cookie'),
]