from django import forms as django_forms
from ..book import forms as book_form
from django.contrib.admin.widgets import AdminDateWidget
from submodules.helper import admin_datepicker_media


class NewOrder(book_form.NewBook):
    class Meta(book_form.NewBook.Meta):
        fields = book_form.NewBook.Meta.fields + (
            'price', 'ordered_at', 'receipt_url')

    price = django_forms.IntegerField()
    ordered_at = django_forms.DateField(widget=AdminDateWidget)
    receipt_url = django_forms.ImageField()

    @property
    def media(self):
        # ここに書いたcss, jsがstaticで呼び出される
        return admin_datepicker_media


class Order(django_forms.Form):
    class Meta:
        fields = book_form.NewBook.Meta.fields + (
            'price', 'ordered_at', 'receipt_url')

    price = django_forms.IntegerField()
    ordered_at = django_forms.DateField(widget=AdminDateWidget)
    receipt_url = django_forms.ImageField()

    @property
    def media(self):
        # ここに書いたcss, jsがstaticで呼び出される
        return admin_datepicker_media
