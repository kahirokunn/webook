from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all(cls) -> list:
        return list(cls.objects.all().order_by('-created_at'))

    @classmethod
    def get_by_id(cls, pk: int):
        return cls.objects.get(pk=pk)

    @classmethod
    def get_by_name(cls, name: str):
        return cls.objects.get(name=name)

    @classmethod
    def is_exists_by_id(cls, pk: int) -> bool:
        return cls.objects.get(pk=pk).exists()

    @classmethod
    def is_exists_by_name(cls, name: str) -> bool:
        return cls.objects.filter(name=name).exists()

    def __str__(self):
        return self.name
