from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('register-space/', views.register_space, name='register_space'),
  path('spaces-list/', views.show_spaces, name='spaces_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)