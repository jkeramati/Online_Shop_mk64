from django.urls import path, include

from order.views import CartListView, CartItemListView

urlpatterns = [
    path('costumer/', CartListView.as_view(), 'cart_list_view'),
    path('Address/', CartItemListView.as_view(), 'cartitem_list_view'),
]