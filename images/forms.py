from django import forms

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image