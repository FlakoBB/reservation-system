from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegister, LoginForm
from .models import MyUser

def register_view(request):
  if request.method == 'POST':
    form = UserRegister(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_admin = False
      user.save()
      return redirect('login')
  else:
    form = UserRegister()
  
  return render(request, 'users/forms/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)

        if user.is_admin:
          return redirect('users_list')
        else:
          return redirect('profile')
      else:
        messages.error(request, 'Usuario no valido')
    else:
      messages.error(request, 'El usuario o la contraseña son incorrectos')
  else:
    form = LoginForm()
  
  return render(request, 'users/forms/login.html', {'form': form})

def profile(request):
  return render(request, 'users/perfil.html')

def show_users(request):
  users = MyUser.objects.all()
  return render(request, 'users/users-list.html', {'users': users})

