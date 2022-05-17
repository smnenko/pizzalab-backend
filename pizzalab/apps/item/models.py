from django.db import models

from django.utils.text import slugify

from core.models import BaseModel
from category.models import Category


class Item(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(null=False, unique=True)
    image = models.URLField()
    description = models.TextField()

    category = models.ForeignKey(
        to=Category,
        null=True,
        related_name='items',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Caloricity(BaseModel):
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbohydrate = models.IntegerField()
    calories = models.IntegerField()

    item = models.OneToOneField(
        to=Item,
        null=True,
        related_name='caloricity',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.item.name if self.item else None} Caloricity'

    class Meta:
        verbose_name_plural = 'caloricities'
