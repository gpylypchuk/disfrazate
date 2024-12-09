from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from .models import Usuario

# Create your views here.
def home(request):
    # print("Usuario autenticado:", request.user)
    print(f"Usuario autenticado: {request.user.is_authenticated}")
    print(f"Nombre de usuario: {request.user.username}")
    templateH=loader.get_template('home.html')
    return HttpResponse(templateH.render())

# Vista para la página de Halloween
def pagina_halloween(request):
    templateHal=loader.get_template('pagina_halloween.html')
    return HttpResponse(templateHal.render())

# Vista para la página de Navidad
def pagina_navidad(request):
    templateNav=loader.get_template('pagina_navidad.html')
    return HttpResponse(templateNav.render())

# Vista para la página de retro
def pagina_retro(request):
    templateRet=loader.get_template('pagina_retro.html')
    return HttpResponse(templateRet.render())

# Vista para la página de Halloween
def pagina_cosplay(request):
    templateCos=loader.get_template('pagina_cosplay.html')
    return HttpResponse(templateCos.render())

# Vista para la página de Navidad
def pagina_heroes(request):
    templateHer=loader.get_template('pagina_heroes.html')
    return HttpResponse(templateHer.render())

# Vista para la página de retro
def pagina_princesas(request):
    templatePrin=loader.get_template('pagina_princesas.html')
    return HttpResponse(templatePrin.render())

def carrito(request):
    templateCar=loader.get_template('carrito.html')
    return HttpResponse(templateCar.render())     
     
def register(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST['name']
        apellido = request.POST['apellido']
        email = request.POST['email']
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        if password == request.POST['2password']:
            # Crear un nuevo usuario
            try:
                user = User.objects.create_user(username=usuario, email=email, password=password)
                user.save()

                # Guardar el usuario en la base de datos
                usuario = Usuario(name=name, apellido=apellido, email=email, usuario=usuario, password=password)
                usuario.save()
            except:
                return render(request, 'registro.html', {'error': 'El usuario ya existe.'})
    
            return redirect('login')  # Redirige a la página de login
        
        else:
            # Si las contraseñas no coinciden, muestra un error
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden.'})
        
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