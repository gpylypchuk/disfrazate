from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def members(request):

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

# Vista para la página de Año Nuevo
def pagina_anio_nuevo(request):
    templateNue=loader.get_template('pagina_ano_nuevo.html')
    return HttpResponse(templateNue.render())

def login(request):
    templateLog=loader.get_template('login.html')
    return HttpResponse(templateLog.render())