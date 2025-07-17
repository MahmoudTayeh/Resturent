from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('phone_number', 'name', 'is_owner', 'is_delivery', 'is_staff', 'is_active')
    list_filter = ('is_owner', 'is_delivery', 'is_staff')
    
    fieldsets = ((None, {'fields': ('phone_number','password')}),
                 ('Personal Info', {'fields':('name','email','address')}),
                 ('Permissions', {'fields':('is_owner', 'is_staff', 'is_delivery', 'is_superuser','groups', 'user_permissions')}),
                 ('Important dates', {'fields':('last_login', 'created_at')}),
                 )
    add_fieldsets = (
    (None, {
        'classes': ('wide',), 
        'fields': (
            'phone_number', 'name', 'email', 'address',
            'password1', 'password2',
            'is_owner', 'is_delivery', 'is_staff', 'is_active'
        ),
    }),
    )

    search_fields = ('phone_number', 'name', 'email')
    ordering = ('-created_at',)

admin.site.register(CustomUser,CustomUserAdmin)