from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
import folium
from folium.plugins import Geocoder
from folium.features import LatLngPopup, ClickForLatLng
min_lon, max_lon = -76, -65
min_lat, max_lat = -56, -17    

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
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
    # Agregar marcadores para cada comentario
    for comentario in comentarios:
        try:
            lat, lon = map(float, comentario.ubicacion.strip("[]").split(","))
            popup_content = f"{comentario.autor}: {comentario.contenido}"
            folium.Marker(location=[lat, lon], popup=popup_content).add_to(m)
        except ValueError:
            # Manejar errores si la ubicación no está en el formato correcto
            pass

    #PLUGINS Y DEMAS
    folium.plugins.Geocoder().add_to(m)
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
    
    #PLUGINS Y DEMAS
    folium.plugins.Geocoder().add_to(m)    

    lat_lng_popup = LatLngPopup()
    m.add_child(lat_lng_popup)
    
    click_for_lat_lng = ClickForLatLng(format_str = '"[" + lat + "," + lng +"]"', alert= True)
    m.add_child(click_for_lat_lng)
    
    context = {'form': form, 'mapap': m._repr_html_()}
    return render(request, 'comentarios/agregar_comentario.html', context)




