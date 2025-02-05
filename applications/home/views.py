from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Prueba

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'

class ListaView(ListView):
    template_name = 'home/list.html'
    queryset = [1,2,3,4,5,6,7,8,9,10,11]
    context_object_name = 'list'

class ModeloPruebaListarView(ListView):
    model = Prueba
    template_name = 'home/prueba.html'
    context_object_name = 'pruebas'
