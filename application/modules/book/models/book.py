from django.db import models
from modules.book.constants import BOOK_TYPES


class Book(models.Model):
    title = models.CharField(max_length=200)
    thumbnail_url = models.URLField(null=True, blank=True)
    orderd_page_url = models.URLField(null=True, blank=True)
    book_url = models.URLField(null=True, blank=True)
    type = models.IntegerField(choices=BOOK_TYPES,
                               default=BOOK_TYPES[1][0])

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all(cls) -> list:
        return list(cls.objects.all())

    @classmethod
    def get(cls, pk: int):
        return cls.objects.get(pk=pk)

    def __str__(self):
        return self.title
