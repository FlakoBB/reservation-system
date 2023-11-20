from django.shortcuts import render, redirect
from .forms import AddSpaceForm
from .models import CoworkingSpace

def register_space(request):
  if request.method == 'POST':
    form = AddSpaceForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('spaces_list')
  else:
    form = AddSpaceForm()

  return render(request, 'spaces/register-space.html', {'form': form})

def show_spaces(request):
  spaces = CoworkingSpace.objects.all()
  return render(request, 'spaces/spaces-list.html', {'spaces': spaces})