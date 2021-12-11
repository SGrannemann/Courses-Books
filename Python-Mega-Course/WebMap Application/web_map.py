"""
A small script from the Python Megacourse.
Creates an interactive html worldmap with a polygon layer as color coding for the
population and a layer with circles that mark volcanoe locations in North America.
Volcanoe markers are clickable and display the volcanoes name and height and lets you
search the volcanoe on Google with a simple click.
"""
import folium
import pandas

# get the locations of the volcanoes within the USA
volcanoe_data = pandas.read_csv(
    'Python-Mega-Course/WebMap Application/Volcanoes.txt')

lats = list(volcanoe_data['LAT'])
longs = list(volcanoe_data['LON'])
elev = list(volcanoe_data['ELEV'])
name = list(volcanoe_data['NAME'])

HTML = """
Volcano name: <br>
<a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
Height: %s m
"""


def elevation_color(elevation: float) -> str:
    """
    Function that returns a color string depending on the elevation of the volcanoe.
    """
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# make a folium map object

base_map = folium.Map(
    location=[52.24531661503799, 8.905503911858245], zoom_start=6)

fgv = folium.FeatureGroup(name='Volcanoes')

# add a marker for each volcanoe location
for lat, lon, el, name in zip(lats, longs, elev, name):
    iframe = folium.IFrame(html=HTML % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(
        iframe), fill_color=elevation_color(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('Python-Mega-Course/WebMap Application/world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
              'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))


# Add the population layers first so the volcanoe layer is "on top" and still clickable
base_map.add_child(fgp)
base_map.add_child(fgv)
base_map.add_child(folium.LayerControl())

base_map.save('Python-Mega-Course/WebMap Application/Map1.html')
