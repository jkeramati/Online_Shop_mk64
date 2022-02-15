from django.urls import path, include

from order.views import CartListView, CartItemListView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart_list_view'),
    path('cartitem/', CartItemListView.as_view(), name='cartitem_list_view'),
]