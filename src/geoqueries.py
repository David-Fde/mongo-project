import src.create_geoindex as geo
import pandas as pd
import src.create_geoindex as geoin

points = {
    'airport_sanjose_ca' : 0.2,
    'train_stations_sanjose_ca' : 0.2,
    'elementary_school_sanjose_ca' : 0.3,
    'kindergarten_sanjose_ca' : 0.3,
    'night_clubs_sanjose_ca' : 0.7,
    'starbucks_sanjose' : 0.5,
    'vegan_restaurants_sanjose_ca' : 0.4        
    }

radius_points = {
    'airport_sanjose_ca' : 10000,
    'train_stations_sanjose_ca' : 2000,
    'elementary_school_sanjose_ca' : 2000,
    'kindergarten_sanjose_ca' : 2000,
    'night_clubs_sanjose_ca' : 500,
    'starbucks_sanjose' : 500,
    'vegan_restaurants_sanjose_ca' : 1000        
    }

def get_points(coll,geoindex,radius):
    near_places = coll.find(
        {"location":
         {"$near":
          {"$geometry":
           geoindex,
            "$maxDistance":radius
           }
          }
        }
    )
    near_places = list(near_places)
    return near_places

def places_radius(name):
    radius = 0
    for x,y in radius_points.items():
        if x == name:
            radius = y
    return radius

def multiply_points(name):
    mult = 0
    for x,y in points.items():
        if x == name:
            mult = y
    return mult

def create_ranking(name):
    db1, coll1 = geoin.connectCollection("companies","startups_sanjose_ca")
    db2, coll2 = geoin.connectCollection("companies",name)
    potential_places = list(coll1.find({"geometry.location.lat":{"$ne":None},"geometry.location.lng":{"$ne":None}}))
    lst=[]
    
    radius = places_radius(name)
    mult = multiply_points(name)    
    for potential_place in potential_places:
        lst.append({
                    'name': potential_place['name'],
                    name : len(get_points(coll2,potential_place['location'],radius)),
                    'total' : (len(get_points(coll2,potential_place['location'],radius))*mult)
                   })
    ranking = pd.DataFrame(lst)
    return ranking
