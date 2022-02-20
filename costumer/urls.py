from django.urls import path, include

from costumer.views import AddressFormView, CostumerSignUpFormView

urlpatterns = [
    path('costumer/', CostumerSignUpFormView.as_view(), name='costumer_signup_view'),
    path('Address/', AddressFormView.as_view(), name='address_form_view'),

]