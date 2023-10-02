from django.urls import path
from inicio.views import inicio, crear_viaje

urlpatterns = [
    path('', inicio),
    path('crear-viaje/<str:ciudad>/<int:costo>', crear_viaje),
]
