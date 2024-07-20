from django import forms
from .models import Obituary

class ObituaryForm(forms.ModelForm):
  class Meta:
    model = Obituary
    fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author', 'image']  # Include image field in form

  # Add custom validation methods for specific fields if needed
