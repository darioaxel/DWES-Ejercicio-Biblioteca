from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Autor

# Create your views here.
class autores_lista(ListView):
    model = Autor
    template_name = 'autor_list.html'
    context_object_name = 'autores'

class crear_autor(CreateView):
    model = Autor
    fields = ['nombre', 'apellidos', 'fecha_nacimiento']
    template_name = 'publicaciones/autor_form.html'
    success_url = '/autores/'