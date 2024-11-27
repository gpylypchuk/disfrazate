from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
