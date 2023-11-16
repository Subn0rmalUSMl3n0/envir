from django.shortcuts import render
import os
import folium
from folium.plugins import geocoder
import pandas as pd
from shapely import wkt
from shapely.geometry import Polygon
from glob import glob

min_lon, max_lon = -76, -65
min_lat, max_lat = -56, -17

def create_polygon_from_wkt(wkt_string):
    # Crea una geometría de tipo Polygon a partir de una cadena WKT
    geom = wkt.loads(wkt_string)
    if geom.geom_type == 'LineString':
        # Si la geometría es LineString, cierra el bucle para formar un polígono
        geom = Polygon(geom)
    return geom

def home (request):
    # Directorio donde se encuentran los archivos CSV
    csv_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'csv_files')

        
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
       #BOUNDS MAPAs
    folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(m)
    folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(m)
    folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(m)
    folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(m)
    
    # Iterar a través de los archivos CSV en la carpeta
    for csv_file in glob(os.path.join(csv_dir, '*.csv')):
        # Cargar el archivo CSV con pandas
        df = pd.read_csv(csv_file)

# Crear un FeatureGroup para este archivo CSV
        fg = folium.FeatureGroup(name=os.path.basename(csv_file), show=False).add_to(m)

        # Iterar a través de las filas del DataFrame
        for index, row in df.iterrows():
            # Obtener la geometría en formato WKT desde la columna "WKT"
            wkt_string = row['WKT']

            # Crea una geometría de tipo Polygon a partir de la cadena WKT
            geom = create_polygon_from_wkt(wkt_string)

            # Agrega la geometría al mapa
            folium.GeoJson(
                geom.__geo_interface__,
                style_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.5, 'color': 'cyan', 'weight':0.5},
            ).add_to(fg)
    folium.LayerControl().add_to(m)
    
    
    #PLUGINS Y DEMAS
    folium.plugins.Geocoder().add_to(m)
    
    
    context = {'mapap': m._repr_html_()}
    
    return render(request,'mapap/home.html', context)
    # Create your views here.


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