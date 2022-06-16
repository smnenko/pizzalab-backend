from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from user.models import Profile
from user.models import Address


@admin.register(get_user_model())
class UsersAdmin(UserAdmin):
    ordering = ('email', 'last_login')
    list_filter = ('created_at', 'updated_at', 'last_login')
    list_display = ('email', 'last_login')
    fieldsets = (
        ('Personal info', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('created_at', 'updated_at', 'last_login')})
    )
    readonly_fields = ('created_at', 'updated_at')
    exclude = ('first_name', 'last_name', 'username', 'is_active')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
