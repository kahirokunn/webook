from django.forms import CharField, ModelForm
from .models.book import Book


class NewForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title',
                  'thumbnail_url',
                  'orderd_page_url',
                  'book_url',
                  'type')

    thumbnail_url = orderd_page_url = book_url = CharField()
