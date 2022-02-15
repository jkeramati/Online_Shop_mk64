from django.urls import path, include

from costumer.views import CostumerFormView, AddressFormView

urlpatterns = [
    path('costumer/', CostumerFormView.as_view(), name='costumer_form_view'),
    path('Address/', AddressFormView.as_view(), name='address_form_view'),

]