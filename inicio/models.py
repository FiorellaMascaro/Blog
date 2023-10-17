from django.db import models

class Viaje(models.Model):
    ciudad = models.CharField(max_length=50)
    costo = models.IntegerField()
    texto = models.TextField(max_length=500, default='')
    
    def __str__(self):
        return f'{self.ciudad} {self.costo} {self.texto}'
 
