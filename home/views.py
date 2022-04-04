from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView
from django.utils.translation import gettext_lazy as _

from home.form import ContactEmailForm
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


# def error_404(request, exception):
#     # data = {}
#     return render(request, '404.html')

class ContactEmailFormView(FormView):
    form_class = ContactEmailForm
    success_url = '/'
    template_name = 'base/_footer.html'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['text']
        send_mail(subject, text, email, ['ali.mashhadi.shop@gmail.com', email])
        if form.is_valid():
            messages.success(self.request, _('Form submission successful'))
        return super().form_valid(form)
