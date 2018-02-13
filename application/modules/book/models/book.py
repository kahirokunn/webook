from django.db import models
from modules.book.constants import BookTypes
from submodules import logger
from submodules.helper import format_enum_to_choices


class Book(models.Model):
    title = models.CharField(max_length=200)
    thumbnail_url = models.ImageField(upload_to='images',
                                      null=True, blank=True)
    orderd_page_url = models.URLField(null=True, blank=True)
    # book_urlは電子本限定。電子本が読めるURLを登録する必要がある。
    book_url = models.URLField(null=True, blank=True)
    type = models.IntegerField(choices=format_enum_to_choices(BookTypes),
                               default=BookTypes.paper)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all(cls) -> list:
        return list(cls.objects.all().order_by('-created_at'))

    @classmethod
    def get(cls, pk: int):
        return cls.objects.get(pk=pk)

    @classmethod
    def get_all_field_names(cls) -> list:
        field_names = [str(field_name)
                       for field_name in cls._meta.get_fields()
                       if '<' not in str(field_name)]
        return list(map(lambda x: x.split('.')[-1], field_names))

    def __str__(self):
        return self.title
