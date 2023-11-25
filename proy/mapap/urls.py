from django.urls import path
from .views import avistamientos
from .views import animales,educativo
from .views import mapa0,mapa1,mapa2, mapa3, mapa4, mapa5, mapa6, mapa7, mapa8, mapa9, mapa10, mapa11, mapa12


urlpatterns = [
    path('', mapa0, name='home'),
    path('avistamientos/',avistamientos,name='avistamientos'),
    path('animales/',animales,name='animales'),
    path('educativo/',educativo,name='educativo'),
    path('mapa1/', mapa1, name='mapa1'),    
    path('mapa2/', mapa2, name='mapa2'),
    path('mapa3/', mapa3, name='mapa3'),    
    path('mapa4/', mapa4, name='mapa4'),
    path('mapa5/', mapa5, name='mapa5'),    
    path('mapa6/', mapa6, name='mapa6'),
    path('mapa7/', mapa7, name='mapa7'),    
    path('mapa8/', mapa8, name='mapa8'),
    path('mapa9/', mapa9, name='mapa9'),    
    path('mapa10/', mapa10, name='mapa10'),
    path('mapa11/', mapa11, name='mapa11'),    
    path('mapa12/', mapa12, name='mapa12'),
]
