from django.urls import path
from inicio.views import inicio, crear_viaje, listado_viajes, editar_viaje, eliminar_viaje, detalle_viaje, about_me

urlpatterns = [
    path('', inicio, name='inicio'),
    path('viajes/', listado_viajes, name='viajes'), 
    path('viajes/crear/', crear_viaje, name='crear_viaje'),
    path('viajes/<int:id_viaje>/editar/', editar_viaje, name='editar_viaje'),
    path('viajes/<int:id_viaje>/eliminar/', eliminar_viaje, name='eliminar_viaje'),
    path('viajes/<int:id_viaje>/detalle/', detalle_viaje, name='detalle_viaje'),
    path('about_me/', about_me, name='about_me'),
]