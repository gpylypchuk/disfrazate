from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto

# Registra el modelo Producto para que aparezca en el Admin
admin.site.register(Producto)