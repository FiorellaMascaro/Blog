from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import NuestroFormularioDeRegistro, NuestroformulariodeEditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def login (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            django_login(request, user)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
            
    formulario = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
    return render(request, 'cuentas/registro.html', {'formulario': formulario})

def editar_perfil(request):
    if request.method == 'POST':
        formulario = NuestroformulariodeEditarPerfil(request.POST, instance=request)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else: 
        formulario = NuestroformulariodeEditarPerfil(instance=request.user)
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class ChangePassword(PasswordChangeView):
    template_name = 'cuentas/editar_pass.html'
    success_url = reverse_lazy('editar_pass') 