from pymongo import MongoClient
from datetime import datetime
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import requests,json,folium
import src.functions as fnc

'''
    Download data of a place from places.api and save them to a .json file.

    #places = pd.DataFrame(fnc.search_places_by_input())
    #places.to_json("./output/dataset.json", orient="records")
'''


def main():
    if __name__=='__main__':
        main()