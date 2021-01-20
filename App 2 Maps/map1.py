import folium
import pandas

#Importamos los datos
data = pandas.read_csv("C:/Users/CeciliaRodríguez/Desktop/Proyectos/Practicas/App 2 Maps/Volcanoes.txt")

#Convertimos los dataframes en Listas 
lon = list(data["LON"])
lat = list(data["LAT"])
ele =  list(data["ELEV"])

#Podemos crear una funcion antes del ciclo for para cambiar el color del marcador de manera dinamica
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    #El tipo de este proyecto es un string por lo tanto se pueden agregar condicionales

#Establecemos la configuracion del mapa, lugar, zoom inicial y tipo de azulejo
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

#Hacemos un grupo para las configuraciones del mapa
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, ele):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" meters", fill=True, fill_color=color_producer(el), color='grey', fill_opacity=0.7))
    #Es importante agregar el fill, fill color, el color que es lo externo del circulo y el fill opacity
#Crea un objeto GeoJson 

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('C:/Users/CeciliaRodríguez/Desktop/Proyectos/Practicas/App 2 Maps/world.json','r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))
#Agregamos las configuraciones al feature group y guardamos el archivo

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("C:/Users/CeciliaRodríguez/Desktop/Proyectos/Practicas/App 2 Maps/MapaDefinitivo.html")