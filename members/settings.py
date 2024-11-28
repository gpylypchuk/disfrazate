DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'disfrazate',
        'USER': 'root',
        'PASSWORD': 'gero2004',   #Contraseña actualizada
        'HOST': 'localhost',  # Cambiar si usas un servidor remoto
        'PORT': '3306',       # Cambiar si usas un puerto diferente
    }
}
INSTALLED_APPS = [
    # otras aplicaciones
    'members',  # Asegúrate de que la aplicación esté aquí
]
