import json
import pymongo
import certifi
from typing import Generic, TypeVar, get_args
from bson import ObjectId

T = TypeVar('T')


class InterfaceRepository(Generic[T]):
    def __init__(self):
        """
        Initializes and stores connections to db and one of its collections as class properties.

        """
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tldCAFile=ca
        )
        self.data_base = client[data_config.get("db-name")]
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()
        self.current_collection = self.data_base.get_collection[self.collection]

    def load_file_config(self):
        """
        Extract db info and url from config.json.

        :return:
        """
        with open("config.json", 'r') as config_file:
            data = json.load(config_file)
        return data

    def find_all(self) -> list:
        dataset = []
        for document in self.current_collection.find():
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)

        return dataset

    def find_by_id(self, id_: str) -> dict:
        _id = ObjectId(id_)
        document = self.current_collection.find_one({"_id": _id})
        document = self.get_values_db_ref(document)

        if document:
            document['_id'] = document['_id'].__str__()
        else:
            document = {}

        return document

    def save(self, item: T) -> T:
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item = item.__dict__
            updated_item = {"$set", item}
            self.current_collection.update_one({'_id': _id}, updated_item)
        else:
            _id = self.current_collection.insert_one(item.__dict__)
            return _id


    def update(self, id_: str, item: T) -> dict:
        pass

    def delete(self, id_: str) -> dict:
        pass

    def query(self, query: dict) -> list:
        pass

    def query_aggregation(self, query: dict) -> list:
        pass

    def get_values_db_ref(self, document) -> T:
        pass

    def get_values_db_ref_from(self, document) -> list:
        pass

    def transform_object_ids(self):
        pass

    def transform_refs(self):
        pass

    def format_list(self):
        pass
