from django import forms
from django.db import models

class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImageInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_image_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_image_clean(d, initial) for d in data]
        else:
            result = single_image_clean(data, initial)
        return result


class ImageFieldForm(forms.Form):
    image_field = MultipleImageField()