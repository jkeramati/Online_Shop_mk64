from django.urls import path, include

# from order.utils import set_cookie
from rest_framework import routers

from order.apies import AddToCart, CartItemList, samplecart, CartUpdateAPI, CartItemDetail, CartItemListApi

router = routers.DefaultRouter()
router.register(r'cartitem', AddToCart)

urlpatterns = [
    path('', include(router.urls)),
    path('cart_off/<int:pk>', CartUpdateAPI.as_view(), name='cart_off_code'),
    path('cart/', CartItemList.as_view(), name='order_item_list'),
    path('cart1/', samplecart, name='order_item_list_sample'),
    path('itemdel/<int:pk>', CartItemDetail.as_view(), name='order_item_detail'),
    path('item/', CartItemListApi.as_view(), name='order_item_list_in_dashboard'),

]
