from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('hola_mundo', views.hola_mundo, name='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path('proyectos/<int:anio>/<int:mes>/', views.ver_proyecto, name='ver_proyecto'),
    path('proyectos/<int:anio>/', views.ver_proyecto, name='ver_proyecto'),
    path('proyectos/', views.ver_proyecto, name='ver_proyecto'),
]