from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('perfil', views.profile, name='profile'),
  path('lista-usuarios/', views.show_users, name='users_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)