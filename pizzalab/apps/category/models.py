from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    parent = models.ForeignKey(
        to='self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.parent if self.parent else ''} {self.name}"

    class Meta:
        verbose_name_plural = 'categories'
