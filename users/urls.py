from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('', views.landing_view, name='landing'),
  path('perfil/', views.profile, name='profile'),
  path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
  path('dashboard/register-admin/', views.admin_register, name='admin_register'),
  path('lista-usuarios/', views.show_users, name='users_list'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.exit, name='exit'),
  path('register/', views.register_view, name='register_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)