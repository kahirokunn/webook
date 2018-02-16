from django.forms import ModelForm
from . import models


class NewMemo(ModelForm):
    class Meta:
        model = models.Memo
        fields = ('text',)
