from django.contrib import admin

# Register your models here.
from discount.models import Discount

admin.register([Discount])
