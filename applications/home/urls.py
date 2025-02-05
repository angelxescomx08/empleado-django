from django.contrib import admin
from django.urls import path
from .views import IndexView, ListView

urlpatterns = [
    path('', IndexView.as_view()),
    path('list/', ListView.as_view()),
]
