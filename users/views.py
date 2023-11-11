from django.shortcuts import render
from .models import User

def profile(request):
  return render(request, 'users/perfil.html')

def show_users(request):
  users = User.objects.all()
  return render(request, 'users/users-list.html', {'users': users})
