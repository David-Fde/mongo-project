from pymongo import MongoClient
import pandas as pd
import src.functions as fnc
import src.create_geoindex as geo

response = input("Download data from api.............. press 1" "\n" 
                "Create geoindex in collection....... press 2" "\n"
                "Print map with points of interest... press 3" "\n"                
                "Exit............................. press E" "\n"
                 )

if int(response) == 1:
    #Download data of a place from places.api and save them to a .json file.

    places = pd.DataFrame(fnc.search_places_by_input())
    places.to_json("./output/dataset.json", orient="records")

elif int(response) == 2:
    # Create a geoindex in a collection downloaded with places API.
    collection = input('Collection name: ')
    print("Creating Geoindex...")
    db, coll = geo.connectCollection('companies',collection)
    places = list(coll.find({"geometry.location.lat":{"$ne":None},"geometry.location.lng":{"$ne":None}}))
    for place in places:
        value = {"$set": {'location':geo.getLocation(place)}}
        coll.update_one(place,value)
    print("Completed")

elif int(response) == 3:
    pass

elif str(response) == "E":
    exit

def main():
    if __name__=='__main__':
        main()