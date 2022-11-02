import json
import pymongo
import certifi
from typing import Generic, TypeVar

T = TypeVar('T')

class InterfaceRepository(Generic[T]):
    def __init__(self) -> None:
        ca = certifi.where()
        data_config = self.load_config()
        client = pymongo.MongoClient(data_config.get('db-connection'), tlsCAFile=ca)

    def load_config(self):
        with open("config.json", "r") as config_file:
            data = json.load(config_file)
        return data
