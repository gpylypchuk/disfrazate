# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.hashers import make_password  # Esto es para encriptar la contraseña

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)  # Usamos set_password para encriptar la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Contraseña encriptada
    date_joined = models.DateTimeField(default=timezone.now)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Usamos el correo como campo único para login
    REQUIRED_FIELDS = ['username']  # El nombre de usuario es requerido

    def __str__(self):
        return self.username

