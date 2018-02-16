from django import forms as django_forms
from ..book import forms as book_form
from django.contrib.admin.widgets import AdminDateWidget
import settings


def admin_datepicker_media():
    extra = '' if settings.DEBUG else '.min'
    css = ('forms.css',)
    js = (
        'vendor/jquery/jquery%s.js' % extra,
        'jquery.init.js',
        'core.js',
        'admin/RelatedObjectLookups.js',
        'actions%s.js' % extra,
        'urlify.js',
        'prepopulate%s.js' % extra,
        'vendor/xregexp/xregexp%s.js' % extra,
        'calendar.js',
        'admin/DateTimeShortcuts.js',
    )
    return django_forms.Media(
        js=['admin/js/%s' % url for url in js],
        css={'all': ['admin/css/%s' % url for url in css]})


class NewOrder(book_form.NewBook):
    class Meta(book_form.NewBook.Meta):
        fields = book_form.NewBook.Meta.fields + ('price', 'ordered_at')

    price = django_forms.IntegerField()
    ordered_at = django_forms.DateField(widget=AdminDateWidget)

    @property
    def media(self):
        # ここに書いたcss, jsがstaticで呼び出される
        return admin_datepicker_media


class Order(django_forms.Form):
    class Meta:
        fields = book_form.NewBook.Meta.fields + ('price', 'ordered_at')

    price = django_forms.IntegerField()
    ordered_at = django_forms.DateField(widget=AdminDateWidget)

    @property
    def media(self):
        # ここに書いたcss, jsがstaticで呼び出される
        return admin_datepicker_media
