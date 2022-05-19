from django.contrib import admin
from django.contrib.auth import get_user_model

from user.models import Profile
from user.models import Address


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
