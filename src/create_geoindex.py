from pymongo import MongoClient

client = MongoClient() # Se pone fuera porque asi es una unica colleccion y va muchisimo mas rapido

def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

def getLocation(lst):       
    longitude = lst['geometry']['location']['lng']
    latitude = lst['geometry']['location']['lat']
    loc = {
        'type':'Point',
        'coordinates':[longitude,latitude]
    }
    return loc

def creating_geoindex(collection_name):
    db, coll = connectCollection('companies',collection_name)
    places = list(coll.find({"geometry.location.lat":{"$ne":None},"geometry.location.lng":{"$ne":None}}))
    for place in places:
        value = {"$set": {'location':getLocation(place)}}
        coll.update_one(place,value)