from django.db import models

class tips(models.Model):
    pais = models.CharField(max_length=80)
    actividad = models.CharField(max_length=80)
    descripcion = models.TextField()
    fecha = models.DateField()
    
    def __str__(self):
        return f'{self.pais} {self.actividad}'
    
