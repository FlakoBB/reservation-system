from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('perfil', views.profile, name='profile'),
  path('lista-usuarios/', views.show_users, name='users_list'),
  path('login/', views.login_view, name='login'),
  path('register/', views.register_view, name='register_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)