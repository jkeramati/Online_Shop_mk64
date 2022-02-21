from django.views.generic import ListView, DetailView
from .models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'cateles'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'catedet'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'


import mixin as mixin

from django.http import JsonResponse, HttpResponse

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from product.models import Product, Category
from product.serializers import ProductSerializer
from django.utils.translation import gettext as _

# def my_view(request):
#     output = _("Welcome to my site.")
#     return HttpResponse(output)
#
#
# @csrf_exempt
# def car_list_api(request):
#     """
#     POST: create Car
#     GET: List Cars
#     :param request:
#     """
#     if request.method == 'GET':
#         product_serializer = ProductSerializer(Product.objects.all(), many=True)
#         return JsonResponse({'data': product_serializer.data}, status=200)
#     elif request.method == 'POST':
#         data = request.POST
#         product_serializer = ProductSerializer(data=data)
#         if product_serializer.is_valid():
#             new_product = product_serializer.save()
#             print(product_serializer.validated_data['brand'])
#             return JsonResponse({'new_car_id': new_product.id}, status=201)
#         else:
#             return JsonResponse({'errors': product_serializer.errors}, status=400)
#     else:
#         return JsonResponse({}, status=405)
#
#
# from rest_framework import mixins
#
#
# class ProductListApi(mixins.ListModelMixin, generics.GenericAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#
# from django.contrib import messages
# from django.views.generic import FormView
# from product.form import ContactForm
#
# from django.urls import reverse_lazy
#
#
# class ContactFormView(FormView):
#     template_name = 'form.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('contact_form')
#
#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, "Form set!")
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         messages.warning(self.request, 'is not correct')
#         return super().form_invalid(form)
#
# #     return HttpResponse("Create!")
