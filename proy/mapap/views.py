from django.shortcuts import render
import folium, requests
from django.template import Template,Context
from django.http import HttpResponse
from .models import Inf_animales
from .forms import BusquedaForm
from django.db.models import Q

min_lon, max_lon = -76, -65
min_lat, max_lat = -56, -17

def home (request):

    #AJUSTES MAPA
    m= folium.Map(location=[-36.552302, -71.889792],
                            zoom_start= 2,
                            zoom_control=False,
                            max_bounds=True,
                            min_zoom=6.5,
                            tiles= "cartodb positron",
                            min_lat=min_lat,
                            max_lat=max_lat,
                            min_lon=min_lon,
                            max_lon=max_lon,
                            ) 
    #BOUNDS MAPA
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(m)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(m)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(m)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(m)
    
    
    folium.TileLayer("stamentoner", show=False).add_to(m)
    folium.LayerControl().add_to(m)

    
    
    context = {'mapap': m._repr_html_()}
    return render(request,'mapap/home.html', context)
# Create your views here.

def avistamientos(request):
    return render(request,'mapap/avistamientos.html')

def animales(request):
    datos = Inf_animales.objects.all()
    form = BusquedaForm()

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            if termino_busqueda:
                datos = datos.filter(
                    Q(nombre__icontains=termino_busqueda) | 
                    Q(habitad__icontains=termino_busqueda)
                )

    return render (request,"mapap/animales.html", {'datos': datos, 'form':form})
