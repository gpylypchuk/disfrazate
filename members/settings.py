DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'disfrazate',
        'USER': 'root',
        'PASSWORD': 'gero2004',
        'HOST': 'localhost',  # Cambiar si usas un servidor remoto
        'PORT': '3306',       # Cambiar si usas un puerto diferente
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Almacena sesiones en la base de datos
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_SECURE = False  # Cambiar a True si usas HTTPS
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1209600  # 2 semanas
