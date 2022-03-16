from django.contrib import admin
from django.urls import path, include

# from product.views import ContactFormView, my_view
from product.apies import *
from product.views import CategoryListView, CategoryDetailView, ProductDetailView, ProductListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list_api/', ProductListAPI.as_view(), name='product_list_api'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('offcode/<int:pk>', OffCodeDetail.as_view(), name='off_code_detail'),
    # path('off_code/', OffCodeAPI.as_view(), name='off_code'),




    # path('cate/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    # path('prod/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # # path('form/', ContactFormView.as_view(), name='contact_form'),
    # # path('trans/', my_view, name='trans'),
    # path('product/list/', ProductListAPI.as_view(), name='product_list1'),
    # path('product/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
    # path('category/list/', CategoryListAPI.as_view(), name='category_list'),
    # path('category/<int:pk>/', CategoryDetailAPI.as_view(), name='category_detail'),
    # path('discount/list/', DiscountListAIE.as_view(), name='discount_list'),
    # path('discount/<int:pk>/', DiscountDetailAPI.as_view(), name='discount_detail'),
    # path('offcode/list/', OffCodeListAIE.as_view(), name='off_code_list'),
    # path('offcode/<int:pk>/', OffCodeDetailAPI.as_view(), name='off_code_detail'),
]
