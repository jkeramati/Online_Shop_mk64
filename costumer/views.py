from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from costumer.form import CostumerSignUpForm, AddressForm


class CostumerSignUpFormView(FormView):
    form_class = CostumerSignUpForm
    template_name = 'costumer/SignUpForm.html'
    success_url = '/costumer/costumer/'

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        login(self.request,form.get_user())
        form.save()
        return super().form_valid(form)


class AddressFormView(FormView):
    form_class = AddressForm
    template_name = ''
