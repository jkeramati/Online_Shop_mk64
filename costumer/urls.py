from django.urls import path, include

from costumer.views import *

urlpatterns = [
    path('login/', CostumerLoginView.as_view(), name='costumer_login_view'),
    path('signup/', CostumerSignUpFormView.as_view(), name='costumer_signup_view'),
    path('signup/success', success_signUp, name='success'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/carthist', CartListAPI.as_view(), name='order_history'),
    path('dashboard/addresslist', AddressAPI.as_view(), name='address_list'),
    path('dashboard/addresslist/add_address', AddFormAddress.as_view(), name='add_address'),
    path('dashboard/addresslist/del_address/<int:pk>', DeleteAddress.as_view(), name='del_address'),
    path('dashboard/profile_info/', ProfileView.as_view(), name='information_profile'),
    path('dashboard/profile_info/edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
    path('dashboard/profile_info/changepass', ChangePasswordFormView.as_view(), name='change_password'),
    path('dashboard/product_list/<int:pk>', ProductForDashboard.as_view(), name='product_dashboard'),
    #
    # path('Address/', AddressFormView.as_view(), name='address_form_view0'),
    # path('address1/', AddressDetailApi.as_view(), name='address_view_detail'),
    # path('address2/', AddressListApi.as_view(), name='address_view_list'),
    # path('costumer1/', CostumerDetailApi.as_view(), name='costumer_view_detail'),
    # path('costumer2/', CostumerListApi.as_view(), name='costumer_view_list'),
]
