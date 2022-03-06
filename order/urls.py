from django.urls import path, include

# from order.context import number_order_cart
from order.views import CartListView, CartItemListView, modal_cart

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart_list_view'),
    path('cartitem/', CartItemListView.as_view(), name='cartitem_list_view'),
    path('cart/', modal_cart, name='modal_cart'),
    path('modal/', modal_cart, name='modal_cart'),
    # path('add_cart/', number_order_cart, name='add_cart'),
]