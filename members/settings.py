import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'disfrazate',
        'USER': 'root',
        'PASSWORD': '1234',   #Contraseña actualizada
        'HOST': 'localhost',  # Cambiar si usas un servidor remoto
        'PORT': '3306',       # Cambiar si usas un puerto diferente
    }
}
INSTALLED_APPS = [
    'members',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

