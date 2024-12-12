from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario, Producto, Carrito, CarritoItem
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.db import IntegrityError


# Vista para la página principal
def home(request):
    return render(request, 'home.html')

# Vista para la página de Halloween
def pagina_halloween(request):
    producto1 = Producto.objects.get(id=11)  # Vampiro
    producto2 = Producto.objects.get(id=24)  # Esqueleto
    producto3 = Producto.objects.get(id=25)  # Bruja
    producto4 = Producto.objects.get(id=26)  # Zombie
    producto5 = Producto.objects.get(id=15)  # Chucky    
    producto6 = Producto.objects.get(id=28)  # Ghostface
    producto7 = Producto.objects.get(id=34)  # Jack Skellington
    producto8 = Producto.objects.get(id=45)  # Diablillo
    producto9 = Producto.objects.get(id=46)  # Vampiresa
    
    return render(request, 'pagina_halloween.html',  {
        'Vampiro': producto1,
        'Esqueleto': producto2,
        'Bruja': producto3,
        'Zombie': producto4,
        'Chucky': producto5,
        'Ghostface': producto6,
        'JackSkellington': producto7,
        'Diablillo': producto8,
        'Vampiresa': producto9,
        })

# Vista para la página de Navidad
def pagina_navidad(request):
    producto1 = Producto.objects.get(id=1)  # PapaNoel
    producto2 = Producto.objects.get(id=21) # Elfo
    producto3 = Producto.objects.get(id=22)  # mama noel
    producto4 = Producto.objects.get(id=23)  # Elfa
    producto5 = Producto.objects.get(id=29)  # grinch    
    producto6 = Producto.objects.get(id=36)  # angel navidad
    
    return render(request, 'pagina_navidad.html',{
        'PapaNoel': producto1,
        'Elfo': producto2,
        'MamaNoel': producto3,
        'Elfa': producto4,
        'Grinch': producto5,
        'Angel': producto6,
        })

# Vista para la página de retro
def pagina_retro(request):
    producto1 = Producto.objects.get(id=16)  #Mario
    producto2 = Producto.objects.get(id=48) #Luigi
    producto3 = Producto.objects.get(id=30)  #Chapulin
    producto4 = Producto.objects.get(id=8)  #Malefica
    producto5 = Producto.objects.get(id=40)  #Aladdin
    producto6 = Producto.objects.get(id=31)  #Minion 
    producto7 = Producto.objects.get(id=27)  #Jerry
    producto8 = Producto.objects.get(id=32)  #Popeye
    producto9 = Producto.objects.get(id=37)  #Mandril
    return render(request, 'pagina_retro.html', {
        'Mario': producto1,
        'Luigi': producto2,
        'Chapulin': producto3,
        'Malefica': producto4,
        'Aladdin': producto5,
        'Minion': producto6,
        'Jerry': producto7,
        'Popeye': producto8,
        'Mandril': producto9,
        })

# Vista para la página de Cosplay
def pagina_cosplay(request):
    producto1 = Producto.objects.get(id=6)  #Vaquero
    producto2 = Producto.objects.get(id=7) #Militar
    producto3 = Producto.objects.get(id=10)  #Pirata
    producto4 = Producto.objects.get(id=13)  #Rey
    producto5 = Producto.objects.get(id=43)  #Disco
    producto6 = Producto.objects.get(id=17)  #Ninja 
    producto7 = Producto.objects.get(id=18)  #Caballero
    producto8 = Producto.objects.get(id=19)  #Policia
    producto9 = Producto.objects.get(id=20)  #Preso
    producto10 = Producto.objects.get(id=44)  #Cisne Negro
    producto11 = Producto.objects.get(id=35)  #Caballero Negro
    producto12 = Producto.objects.get(id=47)  #Hippie
    return render(request, 'pagina_cosplay.html', {
        'Vaquero': producto1,
        'Militar': producto2,
        'Pirata': producto3,
        'Rey': producto4,
        'Disco': producto5,
        'Ninja': producto6,
        'Caballero': producto7,
        'Policia': producto8,
        'Preso': producto9,
        'CisneNegro': producto10,
        'CaballeroNegro': producto11,
        'Hippie': producto12,
        
        } )

# Vista para la página de Héroes
def pagina_heroes(request):
    producto1 = Producto.objects.get(id=2)  #Superman
    producto2 = Producto.objects.get(id=3) #Capitan America
    producto3 = Producto.objects.get(id=4)  #Ironman
    producto4 = Producto.objects.get(id=12)  #Spiderman
    producto5 = Producto.objects.get(id=41)  #Thor
    producto6 = Producto.objects.get(id=42)  #Batman 
    return render(request, 'pagina_heroes.html',{
        'Superman': producto1,
        'CapitanAmerica': producto2,
        'Ironman': producto3,
        'Spiderman': producto4,
        'Thor': producto5,
        'Batman': producto6,
        })

# Vista para la página de Princesas
def pagina_princesas(request):
    producto1 = Producto.objects.get(id=5)  #Blancanieves
    producto2 = Producto.objects.get(id=9) #Tinkerbell
    producto3 = Producto.objects.get(id=14)  #Reina
    producto4 = Producto.objects.get(id=38)  #Bella
    producto5 = Producto.objects.get(id=33)  #Hada Madrina
    producto6 = Producto.objects.get(id=39)  #Cenicienta 
    return render(request, 'pagina_princesas.html',{
        'Blancanieves': producto1,
        'Tinkerbell': producto2,
        'Reina': producto3,
        'Bella': producto4,
        'HadaMadrina': producto5,
        'Cenicienta': producto6,
        })

# Vista para la página del Carrito
@login_required
def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'carrito.html', {'carrito': carrito})

@require_POST
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += int(request.POST.get('cantidad', 1))
    item.save()

    return redirect('carrito')

@require_POST
@login_required
def actualizar_item_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    cantidad = int(request.POST.get('cantidad', 1))
    if cantidad > 0:
        item.cantidad = cantidad
        item.save()
    else:
        item.delete()
    return redirect('carrito')

@require_POST
@login_required
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('carrito')

@require_POST
@login_required
def alternar_alquiler_compra(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    item.es_alquiler = not item.es_alquiler  # Alterna el estado
    item.save()
    return redirect('carrito')


def register(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST['name']
        apellido = request.POST['apellido']
        email = request.POST['email']
        usuario = request.POST['usuario']
        password = request.POST['password']
        confirm_password = request.POST['2password']

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

