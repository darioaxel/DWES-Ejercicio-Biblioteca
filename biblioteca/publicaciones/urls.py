from . import views
from django.urls import path

urlpatterns = [
    path('autores/', views.autores_lista.as_view(), name='autores_lista'),
    path('autores/nuevo/', views.crear_autor.as_view(), name='crear_autor'),
]
