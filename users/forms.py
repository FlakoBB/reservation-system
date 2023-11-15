from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class UserRegister(UserCreationForm):
  first_name = forms.CharField(label='Nombre(s)')
  last_name = forms.CharField(label='Apellido(s)')
  email = forms.EmailField(required=True, label='Correo Electronico')

  class Meta:
    model = MyUser
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class MyLoginForm(forms.Form):
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Tu email, perrra'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Tu contraseña, perra'}))
  
  class Meta:
    model =  MyUser
    fields = ['email', 'password']
