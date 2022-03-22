from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from product.models import Category


# def home(request):
#     return render(request, 'Home.html')


class Home(ListView):
    model = Category
    template_name = 'Home.html'
    context_object_name = 'main_cat'

    def get_queryset(self):
        queryset = Category.objects.filter(parent=None)
        return queryset
