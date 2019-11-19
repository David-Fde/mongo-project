import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

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


