from django import forms
from django.contrib.auth.forms import UserCreationForm as Base
from django.contrib.admin.widgets import AdminDateWidget
from . import models as profile_model
from submodules.helper import admin_datepicker_media
from django.utils.safestring import mark_safe
from django.core.files.images import get_image_dimensions


class NewUserForm(Base):
    class Meta(Base.Meta):
        fields = Base.Meta.fields + ('thumbnail_url', 'join_at',)

    thumbnail_url = forms.ImageField()
    join_at = forms.DateField(widget=AdminDateWidget)

    @property
    def media(self):
        return admin_datepicker_media


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = profile_model.Profile
        fields = ('thumbnail_url', 'join_at')

    join_at = forms.DateField(widget=AdminDateWidget)

    @property
    def media(self):
        return admin_datepicker_media
