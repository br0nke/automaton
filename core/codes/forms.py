from django import forms
from .models import CodeListing
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class CodeListingForm(forms.ModelForm):
    class Meta:
        model = CodeListing
        fields = ('title', 'description', 'category', 'image', 'link')

    def clean_link(self):
        link = self.cleaned_data['link']

        validator = URLValidator()
        try:
            validator(link)
        except ValidationError as e:
            raise ValidationError("Invalid link format. Please enter a valid URL.")

        if 'github.com' not in link.lower():
            raise ValidationError("Link must be from 'github.com'!")

        return link