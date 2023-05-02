from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('reservas', views.reservas, name='reservas'),
    path('servicios', views.servicios, name='servicios'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('crearcuenta',views.crearcuenta, name='crearcuenta'),
    path('recuperarcuenta',views.recuperarContra, name='recuperarcuenta'), 
]