from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='home'),  # Página principal
    path('halloween', views.pagina_halloween, name='pagina_halloween'),  # Página de Halloween
    path('navidad', views.pagina_navidad, name='pagina_navidad'),  # Página de Navidad
    path('retro', views.pagina_retro, name='pagina_retro'),  # Página retro
    path('heroes', views.pagina_heroes, name='pagina_heroes'),  # Página de Halloween
    path('princesas', views.pagina_princesas, name='pagina_princesas'),  # Página de Navidad
    path('cosplay', views.pagina_cosplay, name='pagina_cosplay'),  # Página retro
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
