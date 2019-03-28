import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elevation = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q={0}" target="_blank">{0}</a><br>

<br/>
Height: {1} m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My App')


def marker_color(elevation):
    elevation = int(float(elevation))
    if elevation <= 1000:
        return 'blue'
    if elevation <= 2000:
        return 'green'
    if elevation <= 3000:
        return 'red'


for lat, lon, elevation, name in zip(lat, lon, elevation, name):
    elevation = str(elevation)

    iframe = folium.IFrame(html=html.format(
        name, elevation), width=200, height=100)
    fg.add_child(folium.Marker(
        location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color=marker_color(elevation))))

map.add_child(fg)
map.save('Map1.html')
