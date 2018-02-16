from django import forms
from django.contrib.auth.forms import UserCreationForm as Base
from django.contrib.admin.widgets import AdminDateWidget
from . import models
from submodules.helper import admin_datepicker_media
from django.utils.safestring import mark_safe
from django.core.files.images import get_image_dimensions


class UserForm(Base):
    class Meta(Base.Meta):
        fields = Base.Meta.fields + (
            'thumbnail_url', 'join_at')

    thumbnail_url = forms.ImageField(required=False)
    join_at = forms.DateField(widget=AdminDateWidget)

    @property
    def media(self):
        return admin_datepicker_media
