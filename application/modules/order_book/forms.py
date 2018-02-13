from django.forms import DateField, IntegerField, ModelForm, Media
from .models import OrderBook
from ..book.forms import NewForm as BookForm
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.options import ModelAdmin
from settings import DEBUG


def admin_datepicker_media():
    extra = '' if DEBUG else '.min'
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
    return Media(js=['admin/js/%s' % url for url in js],
                 css={'all': ['admin/css/%s' % url for url in css]})


class NewForm(BookForm):
    price = IntegerField()
    ordered_at = DateField(widget=AdminDateWidget)

    class Meta(BookForm.Meta):
        fields = BookForm.Meta.fields + ('price', 'ordered_at')

    @property
    def media(self):
        # ここに書いたcss, jsがstaticで呼び出される
        return admin_datepicker_media
