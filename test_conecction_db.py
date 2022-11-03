import pymongo
import certifi

import json

def load_config():
    with open("config.json", "r") as config_file:
        data = json.load(config_file)
    return data

ca = certifi.where()
data_config = load_config()
client = pymongo.MongoClient(data_config.get('db-connection'), tlsCAFile=ca)
db = client.test
if db!=None:
    print("Connection successful to MongoDB")
    print("User: ", data_config.get('db-user'))

data_base = client.get_database('results_db')
print(f'Database: {data_base.name}')
print(f'Collections: {data_base.list_collection_names()}')
