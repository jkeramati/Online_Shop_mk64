from django.contrib import admin
from django.urls import path, include
from .views import Home, ContactEmailFormView

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('contact_email', ContactEmailFormView.as_view(), name='send_email'),
]
