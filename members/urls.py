from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('halloween', views.pagina_halloween, name='pagina_halloween'),  # Página de Halloween
    path('navidad', views.pagina_navidad, name='pagina_navidad'),  # Página de Navidad
    path('retro', views.pagina_retro, name='pagina_retro'),  # Página retro
    path('heroes', views.pagina_heroes, name='pagina_heroes'),  # Página de Halloween
    path('princesas', views.pagina_princesas, name='pagina_princesas'),  # Página de Navidad
    path('cosplay', views.pagina_cosplay, name='pagina_cosplay'),  # Página retro
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('carrito', views.carrito, name='carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_item_carrito, name='actualizar_item_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('carrito/alternar/<int:item_id>/', views.alternar_alquiler_compra, name='alternar_alquiler_compra'),
    path('comprar/', views.comprar, name='comprar'),
    path('logout/', views.logout_view, name='logout'),

    # Esto es de prueba se debe adaptar a lo hecho
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),  # Ruta para listar usuarios
]
