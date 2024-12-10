from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=100, default='Desconocido')
    apellido = models.CharField(max_length=100, default='Desconocido')
    email = models.EmailField()
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
