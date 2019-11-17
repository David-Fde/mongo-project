from pymongo import MongoClient
import maps_api

def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

def getLocationMapsApi(company):
    results_json=[]
    for i in range(len(company)):        
        longitude = company[i]['lng']
        latitude = company[i]['lat']
        loc = {         
            'type':'Point',
            'coordinates':[longitude,latitude]
        }
        results_json.append(loc)
    return results_json

db, coll = connectCollection('companies','starbucks')

coords = maps_api.get_coords_from_api()  

for element in coords:
    value = {"$set": {'location':getLocationMapsApi(element)}}
    coll.update_one(element,value)



#to_mongo(coords)
