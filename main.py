import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

velo = pd.read_csv('veloslazdi_visi.csv', encoding="utf-8", delimiter=";", index_col=0)

shapefile = gpd.read_file("./apkaimes/Apkaimes.shp")
map = shapefile.to_crs(epsg=4326)

velo['Apkaime'] = ''

for index, item in velo.iterrows():
    location_raw = item['Atrašanās vieta']
    lat, lon = location_raw.split(', ')
    point = Point(float(lon), float(lat))
    for item in map.geometry.iteritems():
        polygon = item[1]
        if (point.within(polygon)):
            velo.at[index, 'Apkaime'] = map.Name[item[0]]

velo.to_csv('veloslazdi_output.csv')
