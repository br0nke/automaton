from django import forms
from .models import CodeListing

class CodeListingForm(forms.ModelForm):
    class Meta:
        model = CodeListing
        fields = ('title', 'description', 'category', 'image', 'link')

def validate_link(link):
  if "github.com" not in link.lower():
    raise ValueError("Link must be from 'github.com'!")
  
def get_full_url(link):
    if not link.startswith('http'):
        link = f'http://{link}'
    return link