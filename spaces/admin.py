from django.contrib import admin
from .models import SpaceType, CoworkingSpace, Reservation

admin.site.register(SpaceType)
admin.site.register(CoworkingSpace)
admin.site.register(Reservation)
