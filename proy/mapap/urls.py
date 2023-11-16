from django.urls import path
from .views import avistamientos
from .views import animales,educativo
from .views import mapa0,mapa1,mapa2


urlpatterns = [
    path('', mapa0, name='home'),
    path('avistamientos/',avistamientos,name='avistamientos'),
    path('animales/',animales,name='animales'),
    path('educativo/',educativo,name='educativo'),
    path('mapa1/', mapa1, name='mapa1'),    
    path('mapa2/', mapa2, name='mapa2'),
]
