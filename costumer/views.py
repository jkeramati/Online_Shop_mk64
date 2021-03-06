from django.contrib import messages
from django.contrib.auth import login, logout
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, RedirectView, TemplateView, ListView
from django.urls import reverse_lazy
from rest_framework import generics, permissions, authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import User
from costumer.form import CostumerSignUpForm, CostumerLoginForm
from django.utils.translation import gettext_lazy as _

from costumer.models import Address, Costumer
from costumer.permission import IsOwnerPermission
from costumer.serializer import AddressSerializer, CostumerSerializer
from order.models import CartItem, Cart
from product.models import Product
from product.serializers import ProductSerializer
from .utils import send_cartItem_cookie_to_DB


class CartItemList(ListView):
    model = CartItem
    template_name = 'order/samplecart.html'
    context_object_name = 'items'

    def get_queryset(self):
        return CartItem.objects.filter(cart__costumer__user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        total_price = 0
        for item in CartItem.objects.filter(cart__costumer__user=self.request.user):
            total_price += item.product.price * item.number_item
        kwargs['total_price'] = total_price
        kwargs['tax'] = total_price * 0.05
        kwargs['final_price'] = total_price + total_price * 0.05

        return super().get_context_data(object_list=object_list, **kwargs)


class CostumerSignUpFormView(FormView):
    form_class = CostumerSignUpForm
    template_name = 'costumer/SignUp.html'
    success_url = reverse_lazy('success')
    success_message = _("User was created successfully!")

    def form_invalid(self, form):
        print('invalid')
        return super().form_invalid(form)

    def form_valid(self, form):
        print('valid')
        form.save()
        return super().form_valid(form)


def success_signUp(request):
    return render(request, template_name='success.html')


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'costumer/dashboard.html'
    login_url = '/costumer/login/'


class CostumerLoginView(FormView):
    form_class = CostumerLoginForm
    template_name = "costumer/LoginForm.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        url = self.request.GET.get('link', None)
        print('url:', url)
        if url:
            self.success_url = url
        login(self.request, user=form.get_user())
        if self.request.COOKIES.get('cookie_product'):
            send_cartItem_cookie_to_DB(self.request)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ChangePasswordFormView(FormView):
    form_class = PasswordChangeForm
    template_name = 'costumer/dash_change_password.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get(self, request, *args, **kwargs):
        context = {
            'pass': PasswordChangeForm(user=self.request.user)
        }
        template_string = render_to_string(template_name='costumer/dash_change_password.html', context=context)
        return JsonResponse({'password': template_string})

    def form_invalid(self, form):
        print('invalid')
        return super().form_invalid(form)

    def form_valid(self, form):
        print('valid')
        if form.is_valid():
            messages.success(self.request, _('Your password successfully changed!'))
        form.save()
        return super().form_valid(form)


# class ChangePasswordFormView(ListView):
#     model = User
#
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'pass': ChangePasswordForm(),
#         }
#         template_string = render_to_string(template_name='costumer/dash_edit_profile.html', context=context)
#         return JsonResponse({'password': template_string})


# class CostumerLogout(LogoutView)
from django.template.loader import render_to_string
from django.http import JsonResponse


class CartListAPI(ListView):
    model = Cart

    # context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(costumer__user=self.request.user, status="PAY")
        cartitem = CartItem.objects.filter(cart__costumer__user=self.request.user, cart__status="PAY")
        context = {
            'items': cart,
            'items_cart': cartitem,
        }
        template_string = render_to_string(template_name='costumer/dash_history_order.html', context=context)
        return JsonResponse({'cart': template_string})


class AddressAPI(ListView):
    model = Address

    def get(self, request, *args, **kwargs):
        address = Address.objects.filter(costumer__user=self.request.user)
        print(address)
        context = {
            'items': address,
        }
        template_string = render_to_string(template_name='costumer/dash_address_list.html', context=context)
        return JsonResponse({'address': template_string})


class AddFormAddress(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        costumer = Costumer.objects.get(user=self.request.user)
        # print(costumer)
        # # print(costumer,type(costumer))
        request.data['costumer'] = costumer.id
        return super().create(request, *args, **kwargs)


class DeleteAddress(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class EditAddress(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def partial_update(self, request, *args, **kwargs):
        request.data._mutable = True
        costumer = Costumer.objects.get(user=self.request.user)
        request.data['costumer'] = costumer.id
        return super().partial_update(request, *args, **kwargs)


class ProfileView(ListView):
    model = Costumer

    def get(self, request, *args, **kwargs):
        costumer = Costumer.objects.filter(user=self.request.user)
        print(costumer)
        context = {
            'costumer': costumer,
        }
        template_string = render_to_string(template_name='costumer/dash_edit_profile.html', context=context)
        return JsonResponse({'costumer': template_string})


class EditProfile(generics.UpdateAPIView):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(DeleteAddress, self).dispatch(request, *args, **kwargs)

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     # costumer = Costumer.objects.get(user=self.request.user)
    #     # print(costumer)
    #     # kwargs['costumer'] = costumer
    #     return super().create(request, *args, **kwargs)


class ProductForDashboard(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


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


class Logout(RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
