from django.db import models

class Viaje(models.Model):
    ciudad = models.CharField(max_length=50)
    evento = models.CharField(max_length=50)
    costo = models.IntegerField()