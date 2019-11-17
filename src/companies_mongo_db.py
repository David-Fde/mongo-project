from pymongo import MongoClient

def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

def getLocation(company):
    location=[]
    for i in range(len(company['offices'])):        
        longitude = company['offices'][i]['longitude']
        latitude = company['offices'][i]['latitude']
        loc = {
            'type':'Point',
            'coordinates':[longitude,latitude]
        }
        location.append(loc)
    return location   

db, coll = connectCollection('companies','companies')

companies = list(coll.find({"offices.city": "San Jose","founded_year": {"$lt": 2008}
                            ,"offices.longitude":{"$ne":None},"offices.latitude":{"$ne": None}}))

for company in companies:
    value = {"$set": {'location':getLocation(company)}}
    coll.update_one(company,value)