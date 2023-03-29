geolocoder = Nominatim(user_agent = 'South Korea')

def geocoding(address): 
    geo = geolocoder.geocode(address)
    crd = (geo.latitude, geo.longitude)
    print(crd)
    return crd


tags = {'amenity': True}

address_list = ['서울대입구역',
'도림로 264',
'현충로 213']


demo = dict()
for i in address_list: 
    print(i)
    crd = geocoding(i)
    pois = ox.pois.pois_from_point(crd, tags=tags, dist=100)
    poi_count = pois['amenity'].value_counts()    
    demo[i] = poi_count