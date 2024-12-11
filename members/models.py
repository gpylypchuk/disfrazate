from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Usuarios
class Usuario(models.Model):
    name = models.CharField(max_length=100, default='Desconocido')
    apellido = models.CharField(max_length=100, default='Desconocido')
    email = models.EmailField()
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

#########################################################

# Disfraces
class Producto(models.Model):
    id = id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)  # Nombre del producto
    precio_Compra = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    precio_Alquiler = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    #imagen = models.ImageField(upload_to='productos/')  # Imagen del producto
    stock = models.IntegerField()  # Cantidad disponible en stock
    

    def __str__(self):
        return self.nombre