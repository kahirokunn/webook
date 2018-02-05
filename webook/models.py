from django.db import models
from django.utils import timezone

_TYPE_CHOICES = (
    (1, 'e-book'),
    (2, 'paper'),
)


class Books(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    book_type = models.IntegerField(choices=_TYPE_CHOICES, default=None)

    thumbnail_url = models.TextField(null=True, blank=True)
    orderd_page_url = models.TextField(null=True, blank=True)
    book_url = models.TextField(null=True, blank=True)

    ordered_at = models.DateTimeField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    @staticmethod
    def published_list():
        return Books.objects.filter(published_at__lte=timezone.now()).order_by('created_at')

    def __str__(self):
        return self.title
