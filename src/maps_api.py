import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json 
import pandas as pd
import time
apikey = os.getenv("KEY")

def search_places_by_coordinate(location, radius, types):
    
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    places = []
    params = {
        'location': location,
        'radius': radius,
        'types': types,
        'key': apikey
    }
    res = requests.get(endpoint_url, params = params)
    results =  json.loads(res.content)
    places.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
        params['pagetoken'] = results['next_page_token'],
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
    return places






'''
def get_coords_from_api():
    api_key = os.getenv("KEY")

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    query = input('Search query: ')   
    r = requests.get(url + 'query=' + query + '&key=' + api_key) 
    
    x = r.json() 
    y = x['results']    
        
    return pd.DataFrame(y)
    '''
    