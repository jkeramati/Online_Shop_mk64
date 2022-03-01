from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from costumer.models import Costumer, Address


# admin.site.register([Costumer, Address])


class CostumerAdmin(admin.ModelAdmin):
    list_display = ['user', 'fist_name', 'last_name', 'address']
    search_fields = ['user', 'last_name']
    ordering = ['user', 'last_name']


admin.site.register(Costumer, CostumerAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['province', 'city']
    search_fields = ['province', 'city']
    ordering = ['province', 'city']


admin.site.register(Address, AddressAdmin)
