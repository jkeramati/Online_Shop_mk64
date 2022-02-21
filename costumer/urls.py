from django.urls import path, include

from costumer.views import AddressFormView, CostumerSignUpFormView, CostumerLoginView, success_signUp

urlpatterns = [
    path('login/', CostumerLoginView.as_view(), name='costumer_login_view'),
    path('signup/', CostumerSignUpFormView.as_view(), name='costumer_signup_view'),
    path('signup/success', success_signUp, name='signUp'),
    path('Address/', AddressFormView.as_view(), name='address_form_view'),

]