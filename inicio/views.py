from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Viaje

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

def crear_viaje(request):
    
    # viaje = Viaje(ciudad=ciudad, costo=costo) 
    # viaje.save()
    return render(request, r'inicio\crear_viaje.html', {})