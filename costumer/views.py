from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy
from rest_framework import generics, permissions, authentication

from costumer.form import CostumerSignUpForm, AddressForm, CostumerLoginForm
from django.utils.translation import gettext_lazy as _

from costumer.models import Address, Costumer
from costumer.serializer import AddressSerializer, CostumerSerializer


class CostumerSignUpFormView(FormView):
    form_class = CostumerSignUpForm
    template_name = 'costumer/SignUp.html'
    success_url = reverse_lazy('index')
    success_message = _("User was created successfully!")

    def form_invalid(self, form):
        print('invalid')
        return super().form_invalid(form)

    def form_valid(self, form):
        print('valid')
        form.save()
        return super().form_valid(form)


def success_signUp(request):
    return render(request, template_name='Home.html')


class CostumerLoginView(FormView):
    form_class = CostumerLoginForm
    template_name = "costumer/LoginForm.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        login(self.request, user=form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


# class CostumerLogout(LogoutView)


def logout_view(request):
    logout(request)
    return redirect(to=reverse_lazy('index'))


class AddressFormView(FormView):
    form_class = AddressForm
    template_name = ''


from .permission import *


class AddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    authentication_classes = [authentication.BasicAuthentication]


class AddressListApi(generics.ListAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    authentication_classes = [authentication.BasicAuthentication]


class CostumerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CostumerSerializer
    queryset = Costumer.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    authentication_classes = [authentication.BasicAuthentication]


class CostumerListApi(generics.ListAPIView):
    serializer_class = CostumerSerializer
    queryset = Costumer.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsSuperUserPermission]
    authentication_classes = [authentication.BasicAuthentication]
