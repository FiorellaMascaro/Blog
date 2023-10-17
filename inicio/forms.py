from django import forms

class ViajeFormulario(forms.Form):
    ciudad = forms.CharField(max_length=50)
    costo = forms.IntegerField()
    texto = forms.CharField(max_length=500)
    
class CrearViajeFormulario(ViajeFormulario):
    ...

class EditarViajeFormulario(ViajeFormulario):
    ...
    
class ViajeBusquedaFormulario(forms.Form):
    ciudad = forms.CharField(max_length=50, required=False)
    