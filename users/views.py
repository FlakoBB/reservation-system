from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import MyLoginForm, UserRegister
from .models import MyUser

def register_view(request):
  if request.method == 'POST':
    form = UserRegister(request.POST)
    if form.is_valid:
      user = form.save(commit=False)
      user.is_admin = False
      user.save()
      return redirect('login')
  else:
    form = UserRegister()
  
  return render(request, 'users/forms/register.html', {'form': form})

def profile(request):
  return render(request, 'users/perfil.html')

def show_users(request):
  users = MyUser.objects.all()
  return render(request, 'users/users-list.html', {'users': users})

def login_view(request):
  if request.method == 'POST':
    form = MyLoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      
      try:
        user = MyUser.objects.filter(email=email).first()
        if user:
          if user.password != password:
            pass # ? Si la contraseña no es igual...
          else:
            return redirect('profile')
        else:
          pass #? si el usuario no existe...
        
      except MyUser.DoesNotExist:
        user = None        
  else:
    form = MyLoginForm()
  
  return render(request, 'users/forms/login.html', {'form': form})
