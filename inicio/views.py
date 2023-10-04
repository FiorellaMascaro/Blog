from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Viaje
from inicio.forms import ViajeFormulario, ViajeBusquedaFormulario


def inicio (request):
    datos = {
        'fecha': datetime.now()
    }
    
    # template = loader.get_template(r'inicio\inicio.html')
    # template_renderizado = template.render(datos)
    # return HttpResponse(template_renderizado)

    return render(request, r'inicio\inicio.html', datos)

# def crear_viaje(request, ciudad, costo):
    
#     viaje = Viaje(ciudad=ciudad, costo=costo) 
#     viaje.save()
#     return render(request, r'inicio\viaje_creado.html', {})

#def crear_viaje(request):
    
    # viaje = Viaje(ciudad=ciudad, costo=costo) 
    # viaje.save()
    #return render(request, r'inicio\crear_viaje.html', {})

def crear_viaje(request):
    
#    print(request.method)
#    print(request.GET)
#    print(request.POST)
   
   if request.method == 'POST':
        formulario = ViajeFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            viaje = Viaje(ciudad=data.get('ciudad') , costo=request.POST['costo'])
            viaje.save()
        else:
            return render(request, r'inicio\crear_viaje.html', {'formulario': formulario})
 
   formulario = ViajeFormulario()
   return render(request, r'inicio\crear_viaje.html', {'formulario': formulario})

def listado_viajes(request):
    
    formulario = ViajeBusquedaFormulario(request.GET)
    if formulario.is_valid():
        ciudad_a_buscar = formulario.cleaned_data.get('ciudad')
        viajes_encontrados = Viaje.objects.filter(ciudad__icontains=ciudad_a_buscar)
    else:
        viajes_encontrados = Viaje.objects.all()
    
    formulario = ViajeBusquedaFormulario()
    return render(request, r'inicio\listado_viajes.html', {'formulario': formulario, 'viajes_encontrados': viajes_encontrados})