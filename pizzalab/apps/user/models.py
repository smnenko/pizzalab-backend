from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel
from user.managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class Profile(BaseModel):
    user = models.OneToOneField(
        to=get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=13, unique=True)
    birth_date = models.DateField()


class Address(BaseModel):
    user = models.OneToOneField(
        to=get_user_model(),
        related_name='address',
        on_delete=models.CASCADE
    )

    city = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    house = models.IntegerField()
    building = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    apartment = models.IntegerField(null=True, blank=True)
