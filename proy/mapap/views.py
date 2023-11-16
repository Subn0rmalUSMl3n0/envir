# mapap/views.py
from django.shortcuts import render
import folium
import pandas as pd
import folium
from django.conf import settings
from django.shortcuts import render
from shapely import wkt
from shapely.geometry import Polygon
min_lon, max_lon = -76, -65
min_lat, max_lat = -56, -17


def create_polygon_from_wkt(wkt_string):
    # Crea una geometría de tipo Polygon a partir de una cadena WKT
    geom = wkt.loads(wkt_string)
    if geom.geom_type == 'LineString':
        # Si la geometría es LineString, cierra el bucle para formar un polígono
        geom = Polygon(geom)
    return geom

def cargar_y_mostrar_csv(request, csv_file_path, i):
    # Leer datos CSV con pandas
    df = pd.read_csv(csv_file_path)

    # Crear mapa
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
    # Iterar sobre las filas y manejar errores en la conversión de geometrías
    for index, row in df.iterrows():
            # Obtener la geometría en formato WKT desde la columna "WKT"
            wkt_string = row['WKT']

            # Crea una geometría de tipo Polygon a partir de la cadena WKT
            geom = create_polygon_from_wkt(wkt_string)

            # Agrega la geometría al mapa
            folium.GeoJson(
                geom.__geo_interface__,
                style_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.5, 'color': 'cyan', 'weight':0.5},
            ).add_to(m)

    # Convertir el mapa a HTML
    m_html = m._repr_html_()

    m_datos = {"m" + str(i) + "_html": m_html}
    print('mapas/mapa' + str(i) + '.html')
    print('m' + str(i) + '_html')
    return render(request, 'mapas/mapa' + str(i) + '.html', {'m' + str(i) + '_datos': m_datos})

def mapa0(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'AAAAA BASE.csv'
    i=0
    # Llamar a la función para cargar y mostrar el CSV en el mapa
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa1(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Alpaca.csv'
    i=1
    # Llamar a la función para cargar y mostrar el CSV en el mapa
    return cargar_y_mostrar_csv(request, csv_file_path,i)



def mapa2(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Chuncho del Norte.csv'
    i=2
    # Llamar a la función para cargar y mostrar el CSV en el mapa
    return cargar_y_mostrar_csv(request, csv_file_path,i)


def avistamientos(request):
    return render(request,'mapap/avistamientos.html')
def animales(request):
    return render (request,"mapap/animales.html")


#SEGUNDO MAPA
import numpy as np
import random
from folium.plugins import TagFilterButton

def home2 (request): 
        # Generate base data
    data = (np.random.normal(size=(100, 2)) * np.array([[1, 1]]) +
                    np.array([[48, 5]]))
    # Generate the data to segment by (levels of another pandas column in practical usage)
    categories = ['category{}'.format(i+1) for i in range(5)]
    category_column = [random.choice(categories) for i in range(len(data))]   
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
    for i, latlng in enumerate(data):
        category = category_column[i]
        folium.Marker(
            tuple(latlng),
            tags=[category]
        ).add_to(m)
       #BOUNDS MAPA
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(m)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(m)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(m)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(m)
    
    #PLUGINS Y DEMAS
    folium.plugins.Geocoder().add_to(m)
    TagFilterButton(categories).add_to(m)
    


    
    context = {'mapap': m._repr_html_()}
    
    return render(request,'mapap/home2.html', context)

def avistamientos(request):
    return render(request,'mapap/avistamientos.html')
def animales(request):
    return render (request,"mapap/animales.html")
def educativo (request):
    return render (request,'mapap/educativo.html')