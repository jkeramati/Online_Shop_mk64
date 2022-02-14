from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from costumer.form import CostumerForm, AddressForm


class CostumerFormView(FormView):
    form_class = CostumerForm
    template_name = ''


class AddressFormView(FormView):
    form_class = AddressForm
    template_name = ''
