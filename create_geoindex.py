from pymongo import MongoClient
places_coordinates=[]

def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll
    
def mongodb_call():
    db, coll = connectCollection("companies",input("Collection name: "))
    places_coordinates = list(coll.find({"geometry.location.lat":{"$ne":None},"geometry.location.lng":{"$ne":None}}))
    return places_coordinates,coll

def getLocation(places_coordinates):
    location=[]
    for i in range(len(places_coordinates)):        
        longitude = places_coordinates[i]['geometry']['location']['lng']
        latitude = places_coordinates[i]['geometry']['location']['lat']
        loc = {
            'type':'Point',
            'coordinates':[longitude,latitude]
        }
        location.append(loc)
    return location

mongodb_call()
getLocation(places_coordinates)
for place in location:
    value = {"$set": {'location':getLocation(place)}}
    coll.update_one(place,value)