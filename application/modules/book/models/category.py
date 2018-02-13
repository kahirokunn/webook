from django.db import models
from ..models import Book


class Category(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all(cls) -> list:
        return list(cls.objects.all().order_by('-created_at'))

    @classmethod
    def get(cls, name: str):
        return cls.objects.get(name=name)

    @classmethod
    def is_exists(cls, category_name: str) -> bool:
        return cls.objects.filter(name=category_name).exists()

    def __str__(self):
        return self.name
