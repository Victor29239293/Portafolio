from django.shortcuts import render, redirect
from django.views.generic import ListView ,DetailView
from portweb.models import Proyecto
from django.core.mail import send_mail
from django.contrib import messages



class HomeView(ListView):
    template_name = 'base.html'
    model = Proyecto
    context_object_name = 'proyectos'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.all()
        return context
    
    
class ProyectoView(DetailView):
    model = Proyecto
    template_name = 'detalleProyect.html'
    context_object_name = 'proyecto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
