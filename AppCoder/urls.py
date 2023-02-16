#Archivo que maneja las rutas
from django.urls import path

from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('Equipo/', equipos, name='equipos'),
    path('entrenadores/', entrenadores, name='entrenadores'),
    path('jugadores/', jugadores, name='jugadores'),
    path('arbitros/', arbitros, name='arbitros'),
    path('jugador-formulario/', jugador_formulario, name='jugador-formulario'),
    path('entrenador-formulario/', entrenador_formulario, name='entrenador-formulario'),
    path('equipo-formulario/', equipo_formulario, name='equipo-formulario'),
    path('arbitro-formulario/', arbitro_formulario, name='arbitro-formulario'),
    path('busqueda-jugador/', busqueda_jugador, name='busqueda-jugador'),
    path('buscar-jugador/', buscar_jugador, name="buscar-jugador"),
    path('leer-entrenadores/', leer_entrenadores, name='leer-entrenadores'),
    #path('eliminar-entrenador/<entrenador_id>/', eliminar_entrenador, name='eliminar-entrenador'),
    #path('editar-entrenador/<entrenador_id>/', editar_entrenador, name='editar-entrenador'),
    ]

"""urlpatterns = [
    path('', EquipoList.as_view(), name = 'inicio'),
    path('detalle/<pk>', EquipoList.as_view(), name = 'detalle'),
    path('nuevo/', EquipoList.as_view(), name = 'nuevo'),
    path('editar/<pk>', EquipoList.as_view(), name = 'editar'),
    path('eliminar/<pk>', EquipoList.as_view(), name = 'eliminar'),
]"""