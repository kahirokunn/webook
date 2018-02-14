from django.forms import ModelForm, CharField
from .models import Book, Category


class NewBook(ModelForm):
    class Meta:
        model = Book
        fields = ('title',
                  'thumbnail_url',
                  'orderd_page_url',
                  'book_url',
                  'type',
                  'categories',)


class NewCategory(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
