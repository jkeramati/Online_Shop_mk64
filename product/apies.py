from rest_framework import generics

from product.serializers import *


class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.all()
        cate_id = self.request.GET['category_id']
        print(cate_id)
        queryset = queryset.filter(category_id=cate_id)
        print(queryset[0])
        return queryset




    # def get_queryset(self):
    #     off_code = self.request.GET['off_code']
    #     obj_off = OffCode.objects.get(code=off_code)
    #     return obj_off

    # def get_queryset(self):
    #     cate_id = self.request.GET['category_id']
    #     print(cate_id)
    # #     products = Product.objects.filter(category_id=cate_id)
    #     cat1 = Category.objects.filter(id=cate_id)
    #     cat2 = Category.objects.filter(category__category=cat1)
    #     cat3 = Category.objects.filter(category__category__category=cat2)
    #     print(cat1)
    #     print(cat2)
    #     print(cat3)
    #     prodcts1 = Product.objects.filter(category=cat1)
    #     prodcts2 = Product.objects.filter(category=cat2)
    #     prodcts3 = Product.objects.filter(category=cat3)
    #     products=prodcts1+prodcts2+prodcts3

    # return {'data': products}
    # TODO can be costume in filter product is not deleted or ...


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryListAPI(generics.ListCreateAPIView):
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
