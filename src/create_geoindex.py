from pymongo import MongoClient

client = MongoClient() # The call to mongoclient is outside the connecCollection function, 
                        # to only make the call once, and save time and resources.

def connectCollection(database, collection):
    # Get a database and a collection from mongoDB
    db = client[database]
    coll = db[collection]
    return db, coll

def getLocation(lst):       
    # Get the coordinates and create a type point coordinates in mongoDB
    longitude = lst['geometry']['location']['lng']
    latitude = lst['geometry']['location']['lat']
    loc = {
        'type':'Point',
        'coordinates':[longitude,latitude]
    }
    return loc

def creating_geoindex(collection_name):
    # Get all the places, excluding the ones with none values for lat and long.
    # and create a new value location with the type point coordinates from the function getLocation.
    db, coll = connectCollection('companies',collection_name)
    places = list(coll.find({"geometry.location.lat":{"$ne":None},"geometry.location.lng":{"$ne":None}}))
    for place in places:
        value = {"$set": {'location':getLocation(place)}}
        coll.update_one(place,value)