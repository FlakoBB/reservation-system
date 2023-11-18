from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class UserRegister(UserCreationForm):
  first_name = forms.CharField(label='Nombre(s)')
  last_name = forms.CharField(label='Apellido(s)')
  email = forms.EmailField(required=True, label='Correo Electronico')

  class Meta:
    model = MyUser
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
  class Meta:
    model = MyUser
    fields = ['username', 'password']