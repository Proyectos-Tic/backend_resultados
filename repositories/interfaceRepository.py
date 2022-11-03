import json
from bson import ObjectId
import pymongo
import certifi
from typing import Generic, TypeVar, get_args

T = TypeVar('T')

#print(get_args(list[int])[0].__name__)

class InterfaceRepository(Generic[T]):
    def __init__(self) -> None:
        # Connection to MongoDB
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

#==========SPRINT 1 ==========
    def find_all(self) -> list:
        dataset = []
        for document in self.current_collection.find():
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id: str) -> dict:
        _id = ObjectId(id)
        # if document not found, document = None
        document = self.current_collection.find_one({'_id': _id})
        document = self.get_values_db_ref(document)
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            # document not found
            document = {}
        return document

    def save(self, item: T) -> T:
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            # Update
                # item without _id to update
            delattr(item, '_id')
            item = item.__dict__
                # _id filter to update
            id = item._id
            _id = ObjectId(id)
            updated_item = {'$set': item}
            self.current_collection.update_one({'_id': _id}, updated_item)
        else:
            # Insert
            _id = self.current_collection.insert_one(item.__dict__)

    # TODO: Verify the return type
    def update(self, id: str, item: T) -> dict:
        pass

    def delete(self, id: str) -> dict:
        pass

    #Format methods: Secure full compatible with MongoDB <-> Python
    # TODO: Implement the query/format methods in just one method
    def get_values_db_ref(self, document) -> T:
        """
        This method transform sub-documents
        Mongo -> Py

        :param document: Obj from MongoDB
        :return: Obj compatible with Python
        """
        pass

    def get_values_db_ref_from(self, document) -> list:
        """
        Mongo -> Py
        """
        pass

    def transform_object_ids(self):
        """
        This method transform sub-documents
        Mongo -> Py
        """
        pass

    def transform_refs(self):
        """
        Py -> Mongo
        :return:
        """
        pass

#==========SPRINT 2 ==========
    def query(self, query: dict) -> list:
        """
        This method make filtered queries
        """
        pass

    def query_aggregation(self, query: dict) -> list:
        """
        Pylint: queries generated by the database
        """
        pass

    def format_list(self):
        """
        Py -> Mongo
        """
        pass

    def object_to_db_ref(self):
        """
        This method format a list of values, similar to toString() in Java
        """
        pass
