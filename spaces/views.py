from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddSpaceForm
from .models import CoworkingSpace, Reservation

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

def reserve_space(request, space_id):
  space = get_object_or_404(CoworkingSpace, pk=space_id)

  if not space.is_available:
    pass

  space.is_available = False
  space.save()

  reservation = Reservation(user=request.user, space=space)
  reservation.save()

  return redirect('profile')