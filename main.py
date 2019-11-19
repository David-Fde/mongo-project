from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import requests,json,folium
import src.maps_api as ma
apikey = os.getenv("KEY")
#df = ma.get_coords_from_api()   

df = apikey.search_places_by_coordinate("40.819057,-73.914048", "100", "restaurant")

#df.to_csv("./output/dataset.csv", index=False)
print(df)
def main():
    if __name__=='__main__':
        main()