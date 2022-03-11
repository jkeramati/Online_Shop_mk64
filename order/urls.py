from django.urls import path, include

# from order.context import number_order_cart
# from order.utils import set_cookie
from rest_framework import routers

from order.apies import AddToCart, CartItemList
from order.views import CartListView, CartItemListView

router = routers.DefaultRouter()
router.register(r'cartitem', AddToCart)
urlpatterns = [
    path('', include(router.urls)),
    path('cart', CartItemList.as_view(), name='order_item_list')
]
# urlpatterns = [
#     path('cart/', CartListView.as_view(), name='cart_list_view'),
#     # path('cartitem/', AddToCart.as_view(), name='add_to_cart'),
#     # path('cart/', modal_cart, name='modal_cart'),
#     # path('modal/', modal_cart, name='modal_cart'),
#     # path('add_cart/', number_order_cart, name='add_cart'),
#     # path('set_cookie/', set_cookie, name='set_cookie'),
# ]
