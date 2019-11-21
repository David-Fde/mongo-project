from pymongo import MongoClient

def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

def getLocation(lst):
    location=[]       
    longitude = lst['geometry']['location']['lng']
    latitude = lst['geometry']['location']['lat']
    loc = {
        'type':'Point',
        'coordinates':[longitude,latitude]
    }
    location.append(loc)
    return location