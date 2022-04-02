from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from product.models import Category, Product


# def home(request):
#     return render(request, 'Home.html')


class Home(ListView):
    model = Category
    template_name = 'Home.html'

    # context_object_name = 'main_cat'

    # def get_queryset(self):
    #     queryset = Category.objects.filter(parent=None)
    #     return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['last_product'] = Product.objects.all()[6:]
        return super().get_context_data(object_list=object_list, **kwargs)


def error_404(request, exception):
    # data = {}
    return render(request, '404.html')
