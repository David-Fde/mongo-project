import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

def search_places_by_input(query=''):
    apiKey = os.getenv("KEY")
    endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    places = []
    params = {
        'query': input("Query: "),
        'key': apiKey
    }
    res = requests.get(endpoint_url, params = params)
    results = json.loads(res.content)
    places.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
        params['pagetoken'] = results['next_page_token'],
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
    return places


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

def create_geoindex(location,coll):
    for place in location:
        value = {"$set": {'location':getLocation(place)}}
        coll.update_one(place,value)

