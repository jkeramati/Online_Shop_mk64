from django.contrib import admin

# Register your models here.
from costumer.models import Costumer, Address

admin.site.register([Costumer, Address])
