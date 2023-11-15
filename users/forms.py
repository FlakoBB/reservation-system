from django import forms
from .models import User

class MyLoginForm(forms.Form):
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Tu email, perrra'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Tu contraseña, perra'}))
  
  class Meta:
    model =  User
    fields = ['email', 'password']
