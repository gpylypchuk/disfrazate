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
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)  # Nombre del producto
    precio_Compra = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    precio_Alquiler = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    #imagen = models.ImageField(upload_to='productos/')  # Imagen del producto
    stock = models.IntegerField()  # Cantidad disponible en stock
    
    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrito')
    creado_en = models.DateTimeField(auto_now_add=True)

    def total_compra(self):
        total = 0
        for item in self.items.all():
            if item.es_alquiler:
                total += item.total_precio_alquiler()
            else:
                total += item.total_precio_compra()
        return total

    def __str__(self):
        return f"Carrito de {self.usuario.username}"


class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    es_alquiler = models.BooleanField(default=False)

    def total_precio_compra(self):
        return self.producto.precio_Compra * self.cantidad

    def total_precio_alquiler(self):
        return self.producto.precio_Alquiler * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
