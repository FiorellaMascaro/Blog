# from typing import Any
# from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from nuevaapp.models import tips
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

class tipsCreateView(LoginRequiredMixin, CreateView):
    model = tips
    template_name = "nuevaapp/create_tips.html"
    fields = ['pais', 'actividad', 'descripcion', 'fecha']

    def form_valid(self, form):
        form.instance.fecha = date.today()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tips')

class tipsDeleteView(LoginRequiredMixin, DeleteView):
    model = tips
    template_name = "nuevaapp/delete_tips.html"
    success_url = reverse_lazy('tips')
    
class tipsUpdateView(LoginRequiredMixin, UpdateView):
    model = tips
    template_name = "nuevaapp/update_tips.html"
    fields = ['actividad', 'descripcion']
    success_url = reverse_lazy('tips')
    
class tipsDetailView(DetailView):
    model = tips
    template_name = "nuevaapp/detail_tips.html"
    
class tipsListView(ListView):
    model = tips
    context_object_name = 'list_tips'
    template_name = "nuevaapp/list_tips.html"
    
    def get_queryset(self):
        pais = self.request.GET.get('pais', '')
        if pais:
            tips = self.model.objects.filter(pais__icontains=pais)
        else:
            tips = self.model.objects.all()
        return tips