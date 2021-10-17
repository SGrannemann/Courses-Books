import folium
import pandas

# get the locations of the volcanoes within the USA
volcanoe_data = pandas.read_csv('Python-Mega-Course/WebMap Application/Volcanoes.txt')

lats = list(volcanoe_data['LAT'])
longs = list(volcanoe_data['LON'])


# make a folium map object
map = folium.Map(location=[52.24531661503799, 8.905503911858245], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')

# add a marker for each volcanoe location
for lat, lon in zip(lats, longs):
    fg.add_child(folium.Marker(location=[lat, lon], popup='Hi I am a Marker', icon=folium.Icon(color='green')))    



map.add_child(fg)

map.save('Python-Mega-Course/WebMap Application/Map1.html')


