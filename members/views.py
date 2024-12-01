from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
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

# def login(request):
#     templateLog=loader.get_template('login.html')
#     return HttpResponse(templateLog.render())

# def register(request):
#      templateReg=loader.get_template('register.html')
#      return HttpResponse(templateReg.render())

def carrito(request):
    templateCar=loader.get_template('carrito.html')
    return HttpResponse(templateCar.render())     
     
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        apellido = request.POST['apellido']
        email = request.POST['email']
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        if password == request.POST['2password']:
            # Crear un nuevo usuario
            user = User.objects.create_user(username=usuario, email=email, password=password)
            user.save()
            # Guardar el usuario en la base de datos
            usuario = Usuario(name=name, apellido=apellido, email=email, usuario=usuario, password=password)
            usuario.save()
            
            return redirect('login')  # Redirige a la página de login
        else:
            # Si las contraseñas no coinciden, muestra un error
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden.'})
    return render(request, 'register.html')

def registro_exitoso(request):
    templateRegEx=loader.get_template('registro_exitoso.html')
    return HttpResponse(templateRegEx.render())

def listar_usuarios(request):
    # Obtén todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()
    
    # Pasa los usuarios a la plantilla
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']

        # Autenticar al usuario usando el correo electrónico y la contraseña
        user = authenticate(request, username=username, password=password)

        print(f'Usuario: {user}')

        if user is None:
            messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            login(request, user)
            return redirect('home')  # Redirige a la página principal
    
    return render(request, 'login.html')