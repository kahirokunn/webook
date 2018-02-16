from django.forms import ModelForm
from .models import Review


class NewReview(ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'star',)
