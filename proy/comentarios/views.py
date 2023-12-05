from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
import folium
from folium.plugins import Geocoder, LocateControl, MarkerCluster
from folium.features import LatLngPopup, ClickForLatLng
min_lon, max_lon = -76, -65
min_lat, max_lat = -56, -17    

def listar_comentarios(request):
    comentarios = Comentario.objects.all()

    # Inicializa el mapa con ubicación y zoom predeterminados
    m = folium.Map(location=[-36.552302, -71.889792],
                   zoom_start=4,
                   min_zoom=4,
                   zoom_control=False,
                   max_bounds=True,
                   tiles="cartodb positron",
                   min_lat=min_lat,
                   max_lat=max_lat,
                   min_lon=min_lon,
                   max_lon=max_lon,
                   )

    # Agrega plugins y clúster de marcadores
    folium.plugins.LocateControl(auto_start=False).add_to(m)
    folium.plugins.Geocoder().add_to(m)
    marker_cluster = MarkerCluster().add_to(m)

    # Calcula bounding box
    bounds = [[90, 180], [-90, -180]]

    # Agrega marcadores al clúster de marcadores y ajusta bounding box
    for comentario in comentarios:
        try:
            lat, lon = map(float, comentario.ubicacion.strip("[]").split(","))
            popup_content = f"{comentario.autor}: {comentario.contenido}"
            folium.Marker(location=[lat, lon], popup=popup_content).add_to(marker_cluster)

            # Ajusta bounding box
            bounds[0][0] = max(bounds[0][0], lat)
            bounds[0][1] = max(bounds[0][1], lon)
            bounds[1][0] = min(bounds[1][0], lat)
            bounds[1][1] = min(bounds[1][1], lon)
        except ValueError:
            pass

    # Calcula centro y nivel de zoom
    center = [(bounds[0][0] + bounds[1][0]) / 2, (bounds[0][1] + bounds[1][1]) / 2]
    map_zoom = 4  # Ajusta según sea necesario

    # Actualiza mapa con nuevo centro y nivel de zoom
    m.location = center
    m.zoom_start = map_zoom

    context = {'comentarios': comentarios, 'mapa': m._repr_html_()}
    return render(request, 'comentarios/listar_comentarios.html', context)

def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_comentarios')
    else:
        form = ComentarioForm()
        
    
    min_lon, max_lon = -76, -65
    min_lat, max_lat = -56, -17    
    m= folium.Map(location=[-36.552302, -71.889792],
                            zoom_start= 2,
                            zoom_control=False,
                            max_bounds=True,
                            min_zoom=4,
                            tiles= "cartodb positron",
                            min_lat=min_lat,
                            max_lat=max_lat,
                            min_lon=min_lon,
                            max_lon=max_lon,
                            ) 

    
    #PLUGINS Y DEMAS
    folium.plugins.Geocoder().add_to(m)    
    folium.plugins.LocateControl(auto_start=False).add_to(m)

    lat_lng_popup = LatLngPopup()
    m.add_child(lat_lng_popup)
    
    click_for_lat_lng = ClickForLatLng(format_str = '"[" + lat + "," + lng +"]"', alert= True)
    m.add_child(click_for_lat_lng)
    context = {'form': form, 'mapap': m._repr_html_()}
    return render(request, 'comentarios/agregar_comentario.html', context)




