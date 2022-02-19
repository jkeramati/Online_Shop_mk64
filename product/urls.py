from django.contrib import admin
from django.urls import path, include

# from product.views import ContactFormView, my_view
from product.apies import *

urlpatterns = [
    # path('form/', ContactFormView.as_view(), name='contact_form'),
    # path('trans/', my_view, name='trans'),
    path('product/list/', ProductListAIE.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
    path('category/list/', CategoryListAIE.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPI.as_view(), name='category_detail'),
    path('discount/list/', DiscountListAIE.as_view(), name='discount_list'),
    path('discount/<int:pk>/', DiscountDetailAPI.as_view(), name='discount_detail'),
    path('offcode/list/', OffCodeListAIE.as_view(), name='off_code_list'),
    path('offcode/<int:pk>/', OffCodeDetailAPI.as_view(), name='off_code_detail'),
]
