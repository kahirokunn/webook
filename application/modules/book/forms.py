from django.forms import ModelForm
from . import models as book_model


class NewBook(ModelForm):
    class Meta:
        model = book_model.Book
        fields = ('title',
                  'thumbnail_url',
                  'orderd_page_url',
                  'book_url',
                  'type',
                  'categories',)


class NewCategory(ModelForm):
    class Meta:
        model = book_model.Category
        fields = ('name',)


class NewReview(ModelForm):
    class Meta:
        model = book_model.Review
        fields = ('text',
                  'star',)
