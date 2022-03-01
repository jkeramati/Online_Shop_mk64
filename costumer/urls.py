from django.urls import path, include

from costumer.views import *

urlpatterns = [
    path('login/', CostumerLoginView.as_view(), name='costumer_login_view'),
    path('logout/', logout_view, name='costumer_logout'),
    path('signup/', CostumerSignUpFormView.as_view(), name='costumer_signup_view'),
    path('signup/success', success_signUp, name='signUp'),
    path('Address/', AddressFormView.as_view(), name='address_form_view0'),
    path('address1/', AddressDetailApi.as_view(), name='address_view_detail'),
    path('address2/', AddressListApi.as_view(), name='address_view_list'),
    path('costumer1/', CostumerDetailApi.as_view(), name='costumer_view_detail'),
    path('costumer2/', CostumerListApi.as_view(), name='costumer_view_list'),
]