from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User 

class NuestroFormularioDeRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repeat pass', widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {campo: '' for campo in fields}
        
class NuestroformulariodeEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Change email')
    first_name = forms.CharField(label='Change name', max_length= 30)
    last_name = forms.CharField(label='Change family name', max_length= 35)
        
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']