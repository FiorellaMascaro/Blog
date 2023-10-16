from django.db import models
from ckeditor.fields import RichTextField

class tips(models.Model):
    
    pais = models.CharField(max_length=80)
    actividad = models.CharField(max_length=100)
    descripcion = RichTextField()
    fecha = models.DateField()
    
    def __str__(self):
        return f'{self.pais} {self.actividad}'
    
