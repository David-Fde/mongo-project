from pymongo import MongoClient
import pandas as pd
import src.download_from_api as fnc
import src.create_geoindex as geoin
import src.geoqueries as geoq

def main():
    response = input("Download data from api.............. press 1" "\n" 
                    "Create geoindex in collection....... press 2" "\n"
                    "Create ranking by company........... press 3" "\n"                
                    "Exit............................. press E" "\n"
                     )

    if int(response) == 1:
        #Download data of a place from places.api and save them to a .json file.

        places = pd.DataFrame(fnc.search_places_by_input())
        places.to_json("./output/results_api.json", orient="records")

    elif int(response) == 2:
        # Create a geoindex in a collection downloaded with places API.
        collection = input('Collection name: ')
        print("Creating Geoindex...")
        geoin.creating_geoindex(collection)
        print("Completed")

    elif int(response) == 3:
        collections = ["airport_sanjose_ca","elementary_school_sanjose_ca",
                      "kindergarten_sanjose_ca","night_clubs_sanjose_ca", "starbucks_sanjose",
                      "train_stations_sanjose_ca","vegan_restaurants_sanjose_ca"]
        ranking_lst=[]
        for collection in collections:
            ranking_lst.append(geoq.create_ranking(collection))
        total_ranking = ranking_lst[0]
        for i in range(len(ranking_lst)-1):
            total_ranking = total_ranking.merge(ranking_lst[i+1],on='name')
        
        total_ranking.columns = ["name","airport_sanjose_ca","total_airport_sanjose_ca","elementary_school_sanjose_ca",
                                "total_elementary_school_sanjose_ca","kindergarten_sanjose_ca","total_kindergarten_sanjose_ca",
                                "night_clubs_sanjose_ca","total_night_clubs_sanjose_ca", "starbucks_sanjose",
                                "total_starbucks_sanjose","train_stations_sanjose_ca","total_train_stations_sanjose_ca",
                                "vegan_restaurants_sanjose_ca","total_vegan_restaurants_sanjose_ca"]

        total_ranking["final_ranking"] = total_ranking["total_airport_sanjose_ca"] + total_ranking["total_elementary_school_sanjose_ca"] + total_ranking["total_kindergarten_sanjose_ca"] + total_ranking["total_night_clubs_sanjose_ca"] + total_ranking["total_starbucks_sanjose"] + total_ranking["total_train_stations_sanjose_ca"] + total_ranking["total_vegan_restaurants_sanjose_ca"]
        total_ranking = total_ranking.drop(["total_airport_sanjose_ca","total_elementary_school_sanjose_ca","total_kindergarten_sanjose_ca","total_night_clubs_sanjose_ca","total_starbucks_sanjose","total_train_stations_sanjose_ca","total_vegan_restaurants_sanjose_ca"],axis=1)
        total_ranking = total_ranking.sort_values(by=["final_ranking"],ascending=False)
        total_ranking.to_csv("./output/final_ranking.csv",index=False)
    
    elif str(response) == "E":
        exit

if __name__=='__main__':
    main()