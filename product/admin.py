from django.contrib import admin

# Register your models here.
from product.models import *

admin.site.register([Product, Category, Brand, Discount, OffCode, Comment])
