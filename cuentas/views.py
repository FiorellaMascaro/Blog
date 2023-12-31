from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import NuestroFormularioDeRegistro, NuestroformulariodeEditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from cuentas.models import InfoExtra

def login (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            django_login(request, user)
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('crear_viaje')
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

@login_required
def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = NuestroformulariodeEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            info_extra.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'): 
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.save()
            
            formulario.save()
            return redirect('inicio')
    else: 
        formulario = NuestroformulariodeEditarPerfil(initial={'link': info_extra.link, 'avatar': info_extra.avatar}, instance=request.user)
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuentas/editar_pass.html'
    success_url = reverse_lazy('editar_pass') 