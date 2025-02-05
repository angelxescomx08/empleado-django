from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'

class ListView(ListView):
    template_name = 'home/list.html'
    queryset = [1,2,3,4,5,6,7,8,9,10]
    context_object_name = 'list'