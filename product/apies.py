from rest_framework import generics

from product.serializers import *


class ProductListAIE(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()  # TODO can be costume in filter product is not deleted or ...


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryListAIE(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Product.objects.all()  # TODO can be costume in filter product is not deleted or ...


class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Product.objects.all()


class DiscountListAIE(generics.ListCreateAPIView):
    serializer_class = DiscountSerializer
    queryset = Product.objects.all()  # TODO can be costume in filter product is not deleted or ...


class DiscountDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Product.objects.all()


class OffCodeListAIE(generics.ListCreateAPIView):
    serializer_class = OffCodeSerializer
    queryset = Product.objects.all()  # TODO can be costume in filter product is not deleted or ...


class OffCodeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OffCodeSerializer
    queryset = Product.objects.all()
