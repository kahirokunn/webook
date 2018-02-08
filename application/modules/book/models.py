from django.db import models

_TYPE_CHOICES = (
    (1, 'e-book'),
    (2, 'paper'),
)


class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    thumbnail_url = models.TextField(null=True, blank=True)
    orderd_page_url = models.TextField(null=True, blank=True)
    book_url = models.TextField(null=True, blank=True)
    type = models.IntegerField(choices=_TYPE_CHOICES,
                               default=_TYPE_CHOICES[1][0])
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    @classmethod
    def get_all(cls) -> list:
        return cls.objects.all().order_by('created_at')

    def __str__(self):
        return self.title
