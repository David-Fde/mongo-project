from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import requests,json,folium
import src.maps_api as ma

df = ma.get_coords_from_api()   
df.to_csv("./output/dataset.csv", index=False)

def main():
    if __name__=='__main__':
        main()