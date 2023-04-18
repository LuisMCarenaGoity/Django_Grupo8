from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hola_mundo(request):
    return HttpResponse('hola mundo Django')
def index(request):
    return HttpResponse(f"""<h1>PROYECTO DJANGO - CODO A CODO</h1>
                <p>Tes test tes</p>
            """)