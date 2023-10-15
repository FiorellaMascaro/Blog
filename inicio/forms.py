from django import forms

class ViajeFormulario(forms.Form):
    ciudad = forms.CharField(max_length=50)
    costo = forms.IntegerField()
    
class CrearViajeFormulario(ViajeFormulario):
    ...

class EditarViajeFormulario(ViajeFormulario):
    ...
    
class ViajeBusquedaFormulario(forms.Form):
    ciudad = forms.CharField(max_length=50, required=False)
    