from django.contrib import admin
from django.urls import path
from .views import IndexView, ListaView, ModeloPruebaListarView

urlpatterns = [
    path('', IndexView.as_view()),
    path('list/', ListaView.as_view()),
    path('prueba/', ModeloPruebaListarView.as_view()),
]
