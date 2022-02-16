from django.contrib import admin

# Register your models here.
from discount.models import Discount, OffCode

admin.site.register([Discount, OffCode])
