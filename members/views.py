from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from django.contrib.auth.hashers import make_password

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

def login(request):
    templateLog=loader.get_template('login.html')
    return HttpResponse(templateLog.render())

def register(request):
     templateReg=loader.get_template('register.html')
     return HttpResponse(templateReg.render())

def carrito(request):
    templateCar=loader.get_template('carrito.html')
    return HttpResponse(templateCar.render())     
     
def registrar_usuario(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        usuario = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        
        # Encriptar la contraseña
        password = make_password(password)

        # Crear el nuevo usuario
        nuevo_usuario = Usuario(usuario=usuario, email=email, password=password)
        nuevo_usuario.save()

        # Redirigir a una página de éxito o la misma página
        return redirect('registro_exitoso')
    
    return render(request, 'registro.html')

def registro_exitoso(request):
    templateRegEx=loader.get_template('registro_exitoso.html')
    return HttpResponse(templateRegEx.render())

def listar_usuarios(request):
    # Obtén todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()
    
    # Pasa los usuarios a la plantilla
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

# def iniciar_session(request):

# def cerrar_session(request):
