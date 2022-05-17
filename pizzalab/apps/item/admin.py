from django.contrib import admin

from item.models import Item
from item.models import Caloricity


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Caloricity)
class CaloricityAdmin(admin.ModelAdmin):
    pass
