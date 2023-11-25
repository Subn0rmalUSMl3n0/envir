# mapap/views.py
from django.shortcuts import render
import folium
import pandas as pd
import folium
from django.conf import settings
from shapely import wkt
from shapely.geometry import Polygon
from folium.features import ClickForLatLng
from folium.plugins import Geocoder

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
    if i == 0:
        popi = [-36.552302, -71.889792]
    elif i == 1:
        popi = [-22.958393,-68.653564]
    elif i == 2:
        popi = [-18.719097,-70.246582]
    elif i == 3:
        popi = [-30.666266,-70.532227]
    elif i == 4:
        popi = [-41.071069,-73.245850]
    elif i == 5:
        popi = [-41.525030,-71.949463]
    elif i == 6:
        popi = [-43.524655,-74.190674]
    elif i == 7:
        popi = [-38.933776,-72.026367]
    elif i == 8:
        popi = [-40.738933,-72.872314]
    elif i == 9:
        popi = [-42.354485,-73.894043]
    elif i == 10:
        popi = [-33.174426,-70.762937]
    elif i == 11:
        popi = [-23.160563,-67.445068]
    elif i == 12:
        popi = [-45.151053,-72.333984]
    
    # Crear mapa
    m= folium.Map(location = popi,
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

    lat_lng_popup = ClickForLatLng(format_str = '"[" + lat + "," + lng +"]"', alert=False)
    m.add_child(lat_lng_popup)
    # Convertir el mapa a HTML
    m_html = m._repr_html_()

    m_datos = {"m" + str(i) + "_html": m_html}
    print('mapas/mapa' + str(i) + '.html')
    print('m' + str(i) + '_html')
    return render(request, 'mapas/mapa' + str(i) + '.html', {'m' + str(i) + '_datos': m_datos})

def mapa0(request):
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
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa3(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Cóndor.csv'
    i=3
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa4(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Fiu Fiu.csv'
    i=4
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa5(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Lanturn.csv'
    i=5
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa6(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Lobo marino.csv'
    i=6
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa7(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Monito del monte.csv'
    i=7
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa8(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Murcielago Orejon.csv'
    i=8
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa9(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Pudú.csv'
    i=9
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa10(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Puma.csv'
    i=10
    return cargar_y_mostrar_csv(request, csv_file_path,i)
def mapa11(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Vicuña.csv'
    i=11
    return cargar_y_mostrar_csv(request, csv_file_path,i)

def mapa12(request):
    # Ruta al archivo CSV
    csv_file_path = settings.BASE_DIR / 'mapap' / 'csv_files' / 'Zorro gris.csv'
    i=12
    return cargar_y_mostrar_csv(request, csv_file_path,i)







def avistamientos(request):
    return render(request,'mapap/avistamientos.html')
def animales(request):
    return render (request,"mapap/animales.html")



def avistamientos(request):
    return render(request,'mapap/avistamientos.html')
def animales(request):
    return render (request,"mapap/animales.html")
def educativo (request):
    return render (request,'mapap/educativo.html')