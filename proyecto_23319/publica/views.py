from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def hola_mundo(request):
    return HttpResponse('hola mundo Django')
def index(request):
    if(request.method == 'GET'):
        titulo="este titulos es accedido por get"
        
    else:
        titulo="este titulos es accedido por post"

    param_1=request.GET.get('param1')
    return render(request,'publica/index.html',{
       'titulo':titulo,
       'param1':param_1,
       'hoy':datetime.now
    })
    #return HttpResponse(f"""<h1>PROYECTO DJANGO - CODO A CODO</h1>
                #<p>{titulo}</p>
            #""")
def saludar(request,nombre):
    return HttpResponse(f"""
        <h1>hola {nombre}</h1>  
        <p>Tes test tes</p>  
    """)
def ver_proyecto(request,anio=2023,mes=1):
    return HttpResponse(f"""
        <h1>proyectos del mes {mes}/{anio}</h1>  
        <p>listados de proyectos</p>  
    """)