from django.urls import path
from . import views

app_name = 'mi_blog'

urlpatterns = [
    path('familiares/', views.lista_familiares, name='lista_familiares'),
    path('amigos/', views.lista_amigos, name='lista_amigos'),
    path('viajes/', views.lista_viajes, name='lista_viajes'),
    path('familiares/crear/', views.crear_familiar, name='crear_familiar'),
    path('amigos/crear/', views.crear_amigo, name='crear_amigo'),
    path('viajes/crear/', views.crear_viaje, name='crear_viaje'),
    path('buscar/', views.buscar, name='buscar'),
]
