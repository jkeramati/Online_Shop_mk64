import generics as generics
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from .models import Category, Product
from rest_framework import generics
from .serializers import *


class CategoryListView(ListView):
    model = Category
    template_name = 'product/Category.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        category = self.request.GET.get('category', None)
        if category:
            cate_obj = Category.objects.get(name=category)
            qs1 = Product.objects.filter(category=cate_obj)
            qs2 = Product.objects.filter(category__parent=cate_obj)
            qs3 = Product.objects.filter(category__parent__parent=cate_obj)
            qs4 = qs1.union(qs2, all=True)
            qs5 = qs4.union(qs3, all=True)
            kwargs['products'] = qs5
        kwargs['cateles'] = Category.objects.all()
        return super().get_context_data(object_list=object_list, **kwargs)


# class Category

# def get_queryset(self):
#     idd_parent = self.request.GET.get('id_parent')
#     print(idd_parent)
#     return {'data': idd_parent}


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'catedet'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    # def get_context_data(self, **kwargs):
    #     id_product = kwargs['id']
    #     print(id_product)
    #     kwargs['discounted_price'] = Product.price
    #     return super().get_context_data(**kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'product/Category.html'
    context_object_name = 'productles'


class OffCodeCheck(generics.RetrieveAPIView):
    serializer_class = OffCodeSerializer
    queryset = OffCode.objects.all()


class ProductListViewForSinglePage(ListView):
    model = Product

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        category_id = self.request.GET.get('category_id', None)
        print(category_id)
        queryset1 = queryset.filter(category_id=category_id)
        queryset2 = queryset.filter(category__parent_id=category_id)
        queryset3 = queryset.filter(category__parent__parent_id=category_id)
        # print(queryset1)
        # print(queryset2)
        q3 = queryset1.union(queryset2, all=True)
        q4 = q3.union(queryset3, all=True)
        context = {
            'products': q4
        }
        template_string = render_to_string(template_name='product/Category_detail_product.html', context=context)
        return JsonResponse({'products': template_string})


import mixin as mixin

from django.http import JsonResponse, HttpResponse

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from product.models import Product, Category
from product.serializers import ProductSerializer, OffCodeSerializer
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
