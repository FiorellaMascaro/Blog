from django.db import models

class Viaje(models.Model):
    ciudad = models.CharField(max_length=50)
    evento = models.CharField(max_length=50)
    costo = models.IntegerField()
    
def __str__(self):
    return f'{self.ciudad} {self.evento} {self.costo}'