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