from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from AppCoder.models import Equipo, Entrenador, Jugador, Arbitro
from .forms import EquipoFormulario, EntrenadorFormulario, ArbitroFormulario, JugadorFormulario


class EquipoList(ListView):
    model = Equipo
    template_name = 'AppCoder/equipos-list.html'

class EquipoDetalle(DetailView):
    model = Equipo
    template_name = 'AppCoder/equipo-detalle.html'

class EquipoCreacion(CreateView):
    model = Equipo
    template_name = 'AppCoder/equipo-nuevo.html'
    sucess_url = reverse_lazy('inicio')
    fields = ['nombre', 'provincia']

class EquipoUpdate(UpdateView):
    model = Equipo
    template_name = 'AppCoder/equipo-nuevo.html'
    sucess_url = reverse_lazy('inicio')
    fields = ['nombre', 'provincia']

class EquipoDelete(DeleteView):
    model = Equipo
    template_name = 'AppCoder/equipo-eliminar.html'
    sucess_url = reverse_lazy('inicio')
    

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def equipos(request):
    return render(request, 'AppCoder/equipos.html')

def entrenadores(request):
    return render(request, 'AppCoder/entrenadores.html')

def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')

def arbitros(request):
    return render(request, 'AppCoder/arbitros.html')

def equipo_formulario(request):

    if request.method == 'POST':
        mi_formulario = EquipoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_equipo = Equipo(nombre=informacion['nombre'], provincia=informacion['provincia'])
            nuevo_equipo.save()   
            return redirect('inicio')
    
    mi_formulario = EquipoFormulario()

    return render(request, 'AppCoder/equipo-formulario.html', {'formulario_equipo': mi_formulario})

def jugador_formulario(request):

    if request.method == 'POST':
        mi_formulario = JugadorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data 
            jugador_nuevo = Jugador(nombre=informacion['nombre'],
                                 apellido=informacion['apellido'],
                                 peso=informacion['peso'],
                                 altura=informacion['altura'],
                                 equipo=informacion['equipo'],)
            jugador_nuevo.save()
            return redirect('inicio')
    
    mi_formulario = JugadorFormulario()
        
    return render(request, 'AppCoder/jugador-formulario.html', {'formulario_jugador': mi_formulario})



def entrenador_formulario(request):

    if request.method == 'POST':
        mi_formulario = EntrenadorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data 
            entrenador = Entrenador(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                equipo=informacion['equipo'])
            entrenador.save()
            return redirect('inicio')
    
    mi_formulario = EntrenadorFormulario()
        
    return render(request, 'AppCoder/entrenador-formulario.html', {'formulario_entrenador': mi_formulario})

def arbitro_formulario(request):

    if request.method == 'POST':
        mi_formulario = ArbitroFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data 
            arbitro = Arbitro(nombre=informacion['nombre'],
                              apellido=informacion['apellido'],
                              nacionalidad=informacion['nacionalidad'])
            arbitro.save()
            return redirect('inicio')
    
    
    mi_formulario = ArbitroFormulario()
        
    return render(request, 'AppCoder/arbitro-formulario.html', {'formulario_arbitro': mi_formulario})



def busqueda_jugador(request):
    return render(request, 'AppCoder/busqueda-jugador.html')

def buscar_jugador(request):
       
    if request.GET['apellido']:
        mi_apellido = request.GET['apellido']
        resultado = Jugador.objects.filter(apellido__icontains = mi_apellido)

        return render(request, 'AppCoder/resultados-busqueda.html', {'equipos': resultado, 'apellido': mi_apellido})
    else:
        respuesta = 'No ingresaste datos'

    return HttpResponse(respuesta)


def equipos(request):

    mis_equipos = Equipo.objects.all()
        
    if request.method == 'POST':
        mi_formulario = EquipoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            equipo = Equipo(nombre=informacion['nombre'], provincia=informacion['provincia'])
            equipo.save()
            
            nuevo_equipo = {'nombre': informacion['nombre'], 'provincia': informacion['provincia']}
            return render(request, 'AppCoder/equipos.html', {'formulario_equipo': mi_formulario, 'nuevo_equipo': nuevo_equipo, 'mis_equipos': mis_equipos})
    
    else:
        mi_formulario = EquipoFormulario()
    
    return render(request, 'AppCoder/equipos.html', {'formulario_equipo': mi_formulario, 'mis_equipos': mis_equipos})

def leer_entrenadores(request):
    
    entrenadores = Entrenador.objects.all()
    contexto = {'entrenadores': entrenadores}

    return render(request, 'AppCoder/leer-entrenadores.html', contexto)

def eliminar_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    entrenador.delete()

    #Vuelvo al menú
    entrenadores = Entrenador.objects.all()
    contexto = {'entrenadores': entrenadores}

    return render(request, 'AppCoder/leer-entrenadores.html', contexto)

def editar_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)

    if request.method == 'POST':
        mi_formulario = EntrenadorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            entrenador.nombre = informacion['nombre'] 
            entrenador.apellido = informacion['apellido']
            entrenador.equipo = informacion['equipo']

            entrenador.save()
            
            entrenadores = Entrenador.objects.all()
            contexto = {'entrenadores': entrenadores}

            return render(request, 'AppCoder/leer-entrenadores.html', contexto)

    else:
        mi_formulario = EntrenadorFormulario(initial={'nombre': entrenador.nombre, 'apellido': entrenador.apellido, 'equipo': entrenador.equipo})

        entrenadores = Entrenador.objects.all()
        contexto = {'mi_formulario': mi_formulario, 'entrenador_id': entrenador_id, 'entrenadores': entrenador} 

        return render(request, 'AppCoder/leer-entrenadores.html', contexto)