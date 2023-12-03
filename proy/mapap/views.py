# mapap/views.py
from django.shortcuts import render
import folium
import pandas as pd
import folium
from django.conf import settings
from django.shortcuts import render
from shapely import wkt
from shapely.geometry import Polygon
from .models import Inf_animales
from .forms import BusquedaForm
from django.db.models import Q
from shapely import wkt
from folium.features import ClickForLatLng
from folium.plugins import Geocoder, LocateControl

min_lon, max_lon = -76, -65
min_lat, max_lat = -56, -17

def create_polygon_from_wkt(wkt_string):
    geom = wkt.loads(wkt_string)
    if geom.geom_type == 'LineString':
        geom = Polygon(geom)
    return geom

def cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords):    # Leer datos CSV con pandas
    df = pd.read_csv(csv_file_path)

    
    # Crear mapa
    m = folium.Map(
        location=initial_coords,
        zoom_start=2,
        zoom_control=False,
        max_bounds=True,
        min_zoom=6.5,
        tiles="cartodb positron",
        min_lat=min_lat,
        max_lat=max_lat,
        min_lon=min_lon,
        max_lon=max_lon,
    )
    # Iterar sobre las filas y manejar errores en la conversión de geometrías
    for _,row in df.iterrows():
            # Obtener la geometría en formato WKT desde la columna "WKT"
            wkt_string = row['WKT']

            # Crea una geometría de tipo Polygon a partir de la cadena WKT
            geom = create_polygon_from_wkt(wkt_string)

            # Agrega la geometría al mapa
            folium.GeoJson(
                geom.__geo_interface__,
                style_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.5, 'color': 'cyan', 'weight':0.5},
            ).add_to(m)

    #PLUGINS
    folium.plugins.Geocoder().add_to(m)    
    folium.plugins.LocateControl(auto_start=False).add_to(m)

    lat_lng_popup = ClickForLatLng(format_str = '"[" + lat + "," + lng +"]"', alert=False)
    m.add_child(lat_lng_popup)
            
    m_html = m._repr_html_()
    m_datos = {"m" + str(i) + "_html": m_html}
    return render(request,f'mapas/mapa{i}.html',{f'm{i}_datos': m_datos})


def mapa0(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'AAAAA BASE.csv'
    i = 0
    initial_coords = [-36.552302, -71.889792]
    # Llamar a la función para cargar y mostrar el CSV en el mapa
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa1(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Alpaca.csv'
    i = 1
    initial_coords = [-22.958393, -68.653564]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa2(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Chuncho del Norte.csv'
    i = 2
    initial_coords = [-18.719097, -70.246582]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa3(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Cóndor.csv'
    i = 3
    initial_coords = [-30.666266, -70.532227]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa4(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Fiu Fiu.csv'
    i = 4
    initial_coords = [-41.071069, -73.245850]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa5(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Lanturn.csv'
    i = 5
    initial_coords = [-41.525030, -71.949463]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa6(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Lobo marino.csv'
    i = 6
    initial_coords = [-43.524655, -74.190674]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa7(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Monito del monte.csv'
    i = 7
    initial_coords = [-38.933776, -72.026367]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa8(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Murcielago Orejon.csv'
    i = 8
    initial_coords = [-40.738933, -72.872314]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa9(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Pudú.csv'
    i = 9
    initial_coords = [-42.354485, -73.894043]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa10(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Puma.csv'
    i = 10
    initial_coords = [-33.174426, -70.762937]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa11(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Vicuña.csv'
    i = 11
    initial_coords = [-23.160563, -67.445068]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)

def mapa12(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Zorro gris.csv'
    i = 12
    initial_coords = [-45.151053, -72.333984]
    return cargar_y_mostrar_csv(request, csv_file_path, i, initial_coords)



def avistamientos(request):
    return render(request,'mapap/avistamientos.html')

def animales(request):
    datos = Inf_animales.objects.using('mysql').all()
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

def educativo (request):
    return render (request,'mapap/educativo.html')