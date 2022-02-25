from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('phone', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('phone', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    list_editable = ('is_active',)
    search_fields = ('phone',)
    ordering = ('phone',)


admin.site.register(User, CustomUserAdmin)

# @admin.register(User)
# class UesrAdminModel(admin.ModelAdmin):
#     list_display = ['__str__', 'is_superuser', 'is_active']
#     list_editable = ['is_active']
#     search_fields = ['phone']
#     ordering = ['phone']
#     fieldsets = (
#         (None, {'fields': ('phone', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
