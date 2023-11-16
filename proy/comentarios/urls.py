from django.urls import path
from .views import listar_comentarios, agregar_comentario

urlpatterns = [
    path('listar/', listar_comentarios, name='listar_comentarios'),
    path('agregar/', agregar_comentario, name='agregar_comentario'),
]
