from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'publica/index.html',{})
    #return HttpResponse(f"""<h1>PROYECTO DJANGO - CODO A CODO</h1>
                #<p>{titulo}</p>
            #""")
def reservas(request):
    return render(request,'publica/Reservas.html',{})

def contacto(request):
    return render(request,'publica/contacto.html',{})


def crearcuenta(request):
    return render(request,'publica/crearCuenta.html',{})

def login(request):
    return render(request,'publica/login.html',{})

def nosotros(request):
    return render(request,'publica/nosotros.html',{})

def galeria(request):
    return render(request,'publica/Fotos.html',{})

def recuperarContra(request):
    return render(request,'publica/recuperarContrasena.html',{})

def servicios(request):
    return render(request,'publica/Servicios.html',{})
