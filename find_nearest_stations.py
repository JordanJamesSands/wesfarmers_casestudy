
import geopy.distance
import pandas as pd

bunnings_latlon = (-37.9003340275206, 145.12698915589579)
officeworks_latlon = (-38.14841478301936, 144.36390415590225)
kmart_latlon = (-31.96532953131573, 115.93558156924325)

def find_nearest_station(latlon):
    stations = pd.read_fwf('data/tables/stations_db.txt',header=None)
    stations.columns = ['ID','state','code1','Station Name','code2','lat','lon']
    min_dist = 80000 #start with twice the circumference of the Earth
    closest_station = None
    for row in stations.iterrows():
        station_latlon = (row[1]['lat'],row[1]['lon'])
        dist = geopy.distance.distance(station_latlon,latlon)
        dist_km = dist.km
        if min_dist > dist_km:
            min_dist = dist_km
            closest_station = row[1]['Station Name']
    print('Closest station is {} at {} Km'.format(closest_station,min_dist))
    return closest_station

find_nearest_station(bunnings_latlon)
find_nearest_station(officeworks_latlon)
find_nearest_station(kmart_latlon)
