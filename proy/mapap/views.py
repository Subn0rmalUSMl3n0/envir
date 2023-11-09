from django.shortcuts import render
import os
import folium
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
    #BOUNDS MAPA
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

    context = {'mapap': m._repr_html_()}
    return render(request, 'mapap/home.html', context)
