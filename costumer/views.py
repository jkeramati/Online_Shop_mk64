from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy
from costumer.form import CostumerSignUpForm, AddressForm, CostumerLoginForm
from django.utils.translation import gettext_lazy as _


class CostumerSignUpFormView(FormView):
    form_class = CostumerSignUpForm
    template_name = 'costumer/SignUpForm.html'
    success_url = '/costumer/signup/'
    success_message = _("User was created successfully!")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CostumerLoginView(FormView):
    form_class = CostumerLoginForm
    template_name = "costumer/LoginForm.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        login(self.request, user=form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddressFormView(FormView):
    form_class = AddressForm
    template_name = ''
