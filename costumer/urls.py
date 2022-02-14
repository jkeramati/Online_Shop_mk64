from django.urls import path, include

from costumer.views import CostumerFormView, AddressFormView

urlpatterns = [
    path('costumer/', CostumerFormView.as_view(), 'costumer_form_view'),
    path('Address/', AddressFormView.as_view(), 'address_form_view'),

]