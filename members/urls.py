from django.urls import path
from . import views

urlpatterns = [
    path('home', views.members, name='home'),
    path('halloween', views.pagina_halloween, name='pagina_halloween'),  # Página de Halloween
    path('navidad', views.pagina_navidad, name='pagina_navidad'),  # Página de Navidad
    path('ano_nuevo', views.pagina_anio_nuevo, name='pagina_ano_nuevo'),  # Página de Año Nuevo
    path('login', views.login, name='login'),
]
