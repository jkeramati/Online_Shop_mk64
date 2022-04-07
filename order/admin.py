from django.contrib import admin

# Register your models here.
from order.models import CartItem, Cart

admin.site.register([Cart, CartItem])
