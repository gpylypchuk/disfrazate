from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usuario
from django.template.loader import render_to_string
from django.contrib.auth import logout
from django.db import IntegrityError


# Vista para la página principal
def home(request):
    return render(request, 'home.html')

# Vista para la página de Halloween
def pagina_halloween(request):
    return render(request, 'pagina_halloween.html')

# Vista para la página de Navidad
def pagina_navidad(request):
    return render(request, 'pagina_navidad.html')

# Vista para la página de retro
def pagina_retro(request):
    return render(request, 'pagina_retro.html')

# Vista para la página de Cosplay
def pagina_cosplay(request):
    return render(request, 'pagina_cosplay.html')

# Vista para la página de Héroes
def pagina_heroes(request):
    return render(request, 'pagina_heroes.html')

# Vista para la página de Princesas
def pagina_princesas(request):
    return render(request, 'pagina_princesas.html')

# Vista para la página del Carrito
def carrito(request):
    return render(request, 'carrito.html')
    
     
# def register(request):
#     if request.method == 'POST':
#         # Obtener los datos del formulario
#         name = request.POST['name']
#         apellido = request.POST['apellido']
#         email = request.POST['email']
#         usuario = request.POST['usuario']
#         password = request.POST['password']
        
#         if password == request.POST['2password']:
#             # Crear un nuevo usuario
#             try:
#                 user = User.objects.create_user(username=usuario, email=email, password=password)
#                 user.save()

#                 # Guardar el usuario en la base de datos
#                 usuario = Usuario(name=name, apellido=apellido, email=email, usuario=usuario, password=password)
#                 usuario.save()
#             except:
#                 return render(request, 'registro.html', {'error': 'El usuario ya existe.'})
    
#             return redirect('login')  # Redirige a la página de login
        
#         else:
#             # Si las contraseñas no coinciden, muestra un error
#             return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden.'})
        
#     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST['name']
        apellido = request.POST['apellido']
        email = request.POST['email']
        usuario = request.POST['usuario']
        password = request.POST['password']
        confirm_password = request.POST['2password']
        # print(name)
        # print(apellido)
        # print(email)
        # print(usuario)
        # print(password)
        # print(confirm_password)
        
        # Validar que las contraseñas coincidan
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden.'})
        
        try:
            # Crear un nuevo usuario
            user = User.objects.create_user(username=usuario, email=email, password=password)
            user.save()

            # Guardar datos adicionales en la base de datos (si tienes un modelo extra)
            usuario_extra = Usuario(name=name, apellido=apellido, email=email, usuario=usuario)
            usuario_extra.save()

            return redirect('login')  # Redirige a la página de login
        except IntegrityError:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden.'})
        

    # Si no es un POST, muestra el formulario vacío
    return render(request, 'register.html')

def listar_usuarios(request):
    # Obtén todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()
    
    # Pasa los usuarios a la plantilla
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def login_view(request):
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña del formulario
        username = request.POST['usuario']
        password = request.POST['password']

        # Autenticar al usuario usando el correo electrónico y la contraseña
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            login(request, user)
            print(request.user)
            return redirect('home')  # Redirige a la página principal
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')