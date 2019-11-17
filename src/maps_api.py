import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json 

def get_coords_from_api():
    api_key = os.getenv("KEY")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    query = input('Search query: ') 
    r = requests.get(url + 'query=' + query +
                            '&key=' + api_key) 
    x = r.json() 
    y = x['results']
    results_maps_api = []
    for i in range(len(y)):   
        results_maps_api.append(y[i]['geometry']['location'])
    return results_maps_api
