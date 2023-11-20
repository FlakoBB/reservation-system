from django import forms
from .models import CoworkingSpace

class AddSpaceForm(forms.ModelForm):
  class Meta:
    model = CoworkingSpace
    fields = '__all__'