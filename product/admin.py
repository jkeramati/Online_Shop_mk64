from django.contrib import admin

# Register your models here.
from product.models import *

admin.register([Product, Category, Brand])
