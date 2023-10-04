from django.urls import path
from inicio.views import inicio, crear_viaje, listado_viajes

urlpatterns = [
    path('', inicio, name='inicio'),
   # path('crear-viaje/<str:ciudad>/<int:costo>', crear_viaje, name= 'crear_viaje'),
    path('viajes/', listado_viajes, name='viajes'), 
    path('viajes/crear/', crear_viaje, name='crear_viaje'),
]
