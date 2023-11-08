from django.urls import path
from .views import home,avistamientos
from .views import animales

urlpatterns = [
    path('', home, name='home'),
    path('avistamientos/',avistamientos,name='avistamientos'),
    path('animales/',animales,name='animales')
]
