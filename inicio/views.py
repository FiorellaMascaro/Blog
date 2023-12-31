from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Viaje
from inicio.forms import ViajeFormulario, ViajeBusquedaFormulario, EditarViajeFormulario, CrearViajeFormulario
from django.contrib.auth.decorators import login_required

def inicio (request):
    datos = {
        'fecha': datetime.now()
    }
    return render(request, r'inicio\inicio.html', datos)

@login_required
def crear_viaje(request):
   if request.method == 'POST':
        formulario = CrearViajeFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            viaje = Viaje(ciudad=data.get('ciudad') , costo=data['costo'], texto=data.get('texto') )
            viaje.save()
            return redirect('viajes')
        else:
            return render(request, r'inicio\crear_viaje.html', {'formulario': formulario})
   formulario = ViajeFormulario()
   return render(request, r'inicio\crear_viaje.html', {'formulario': formulario})

@login_required
def editar_viaje(request, id_viaje):
    editar_viaje = Viaje.objects.get(id=id_viaje)
    
    if request.method == 'POST':
        formulario = EditarViajeFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            editar_viaje.ciudad = data['ciudad']
            editar_viaje.costo = data['costo']
            editar_viaje.texto = data['texto']
            editar_viaje.save()
            return redirect('viajes')
        
        else:
            return render(request, 'inicio/editar_viaje.html', {'formulario': formulario})
        
    formulario = EditarViajeFormulario(initial={'ciudad': editar_viaje.ciudad, 'costo': editar_viaje.costo, 'texto': editar_viaje.texto})
    return render(request, r'inicio/editar_viaje.html', {'formulario': formulario})


def listado_viajes(request):
    formulario = ViajeBusquedaFormulario(request.GET)
    if formulario.is_valid():
        ciudad_a_buscar = formulario.cleaned_data.get('ciudad')
        viajes_encontrados = Viaje.objects.filter(ciudad__icontains=ciudad_a_buscar)
    else:
        viajes_encontrados = Viaje.objects.all()
    
    formulario = ViajeBusquedaFormulario()
    return render(request, r'inicio\listado_viajes.html', {'formulario': formulario, 'viajes_encontrados': viajes_encontrados})


@login_required
def eliminar_viaje(request, id_viaje):
    eliminar_viaje = Viaje.objects.get(id=id_viaje)
    eliminar_viaje.delete()
    
    return redirect('viajes')

def detalle_viaje(request, id_viaje):
    viaje = Viaje.objects.get(id=id_viaje)
    return render(request, 'inicio/detalle_viaje.html', {'viaje': viaje})

def about_me(request):
    return render(request, 'inicio/about_me.html')