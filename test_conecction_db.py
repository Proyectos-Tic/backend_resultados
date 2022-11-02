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
print(db)

print(client.list_database_names())
data_base = client['results_db']
print(data_base.list_collection_names())
