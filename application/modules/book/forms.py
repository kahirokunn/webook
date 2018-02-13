from django.forms import URLField, ModelForm
from .models import Book


class NewForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title',
                  'thumbnail_url',
                  'orderd_page_url',
                  'book_url',
                  'type')
