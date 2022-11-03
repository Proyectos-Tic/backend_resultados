import json
import pymongo
import certifi
from typing import Generic, TypeVar, get_args

T = TypeVar('T')

print(get_args(list[int])[0].__name__)

class InterfaceRepository(Generic[T]):
    def __init__(self) -> None:
        ca = certifi.where()
        data_config = self.load_config()
        client = pymongo.MongoClient(
            data_config.get('db-connection'), 
            tlsCAFile=ca)

        self.data_base = client.get_database(data_config.get('db-name'))
        # Class name of the generic type: <class 'Mesas'>
        model_class = get_args(self.__orig_bases__[0])
        # Use the class name to get the collection: Mesas(model) -> mesas(collection)
        self.collection = model_class[0].__name__.lower()
        self.current_collection = self.data_base.get_collection(self.collection)

    def load_config(self):
        with open("config.json", "r") as config_file:
            data = json.load(config_file)
        return data
