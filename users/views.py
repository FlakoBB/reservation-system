from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegister, LoginForm
from .models import MyUser
from spaces.models import Reservation

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
          return redirect('admin_dashboard')
        else:
          return redirect('profile')
      else:
        messages.error(request, 'Usuario no valido')
    else:
      messages.error(request, 'El usuario o la contraseña son incorrectos')
  else:
    form = LoginForm()
  
  return render(request, 'users/forms/login.html', {'form': form})

@login_required
def admin_dashboard(request):
  if not request.user.is_admin:
    return redirect('profile')
  
  return render(request, 'users/admin-dashboard.html')

@login_required
def admin_register(request):
  if not request.user.is_admin:
    return redirect('profile')
  
  if request.method == 'POST':
    form = UserRegister(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_admin = True
      user.save()
      return redirect('login')
  else:
    form = UserRegister()
  
  return render(request, 'users/forms/admin-register.html', {'form': form})

@login_required
def profile(request):
  user = request.user
  spaces = Reservation.objects.filter(user=request.user)
  return render(request, 'users/perfil.html', {'user': user, 'spaces': spaces})

def landing_view(request):
  return render(request, 'users/landing.html')

def exit(request):
  logout(request)
  return redirect('landing')

def show_users(request):
  users = MyUser.objects.all()
  return render(request, 'users/users-list.html', {'users': users})

