"""Online_Shop_mk64 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
                  path('', include('home.urls')),
                  path('admin/', admin.site.urls),
                  path('costumer/', include('costumer.urls')),
                  path('order/', include('order.urls')),
                  path('product/', include('product.urls')),
                  re_path(r'^rosetta/', include('rosetta.urls')),
                  path('i18n/', include('django.conf.urls.i18n')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('costumer/', include('costumer.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),

    # اگر این مقدار وارد نشود یا برابر مقدار صحیح قرار گیرد
    # می بایست زبان اصلی و پیشفرض پروژه را نیز در آدرس ها قرار دهیم
    # /fa/ , /en/ , ....
    prefix_default_language=False,
)
