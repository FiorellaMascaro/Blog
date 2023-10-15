from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from nuevaapp.models import tips
from django.urls import reverse_lazy

class tipsCreateView(CreateView):
    model = tips
    template_name = "nuevaapp/create_tips.html"
    fields = ['pais', 'actividad', 'descripcion', 'fecha']
    success_url = reverse_lazy('tips')

class tipsDeleteView(DeleteView):
    model = tips
    template_name = "nuevaapp/delete_tips.html"
    success_url = reverse_lazy('tips')
    
class tipsUpdateView(UpdateView):
    model = tips
    template_name = "nuevaapp/update_tips.html"
    fields = ['actividad', 'descripcion']
    success_url = reverse_lazy('tips')
    
class tipsDetailView(DetailView):
    model = tips
    template_name = "nuevaapp/detail_tips.html"
    
class tipsListView(ListView):
    model = tips
    context_object_name = 'ListView'
    template_name = "nuevaapp/list_tips.html"
