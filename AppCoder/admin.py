from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Entrenador)
admin.site.register(Arbitro)


