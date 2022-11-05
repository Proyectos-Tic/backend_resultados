import json
from bson import ObjectId, DBRef
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
    def find_all(self, query: dict = {}) -> list:
        dataset = []
        for document in self.current_collection.find(query):
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
                # _id filter to update
            id = item._id
            _id = ObjectId(id)
                # item without _id to update
            delattr(item, '_id')
            item = item.__dict__
            updated_item = {'$set': item}
            self.current_collection.update_one({'_id': _id}, updated_item)
        else:
            # Insert
            result = self.current_collection.insert_one(item.__dict__)
            id = result.inserted_id.__str__()
        return self.find_by_id(id)

    # TODO: Verify the return type and check if it is necessary to implement the method
    def update(self, id: str, item: T) -> dict:
        _id = ObjectId(id)
        item_dict = item.__dict__
        updated_item = {'$set': item_dict}
        result = self.current_collection.update_one({'_id': _id}, updated_item)
        # TODO check what could be the best response
        return {'Updated_count': result.matched_count}

    def delete(self, id: str) -> dict:
        _id = ObjectId(id)
        result = self.current_collection.delete_one({'_id': _id})
        return {'Deleted_count': result.deleted_count}

    #Format methods: Secure full compatible with MongoDB <-> Python
    # TODO: Implement the query/format methods in just one method
    def get_values_db_ref(self, document) -> T:
        """
        This method transform sub-documents
        Mongo -> Py

        :param document: Obj from MongoDB
        :return: Obj compatible with Python
        """
        for key in document.keys():
            value = document.get(key)
            if isinstance(value, DBRef):
                collection_ref = self.data_base.get_collection(value.collection)
                _id = ObjectId(value.id)
                document_ref = collection_ref.find_one({'_id': _id})
                document_ref['_id'] = document_ref['_id'].__str__()
                # TODO: Change order
                document[key] = document_ref
                document[key] = self.get_values_db_ref(document[key])
            elif isinstance(value,list) and len(list) > 0:
                document[key] = self.get_values_db_ref_from_list(value)
            elif isinstance(value, dict):
                document[key] = self.get_values_db_ref(value)
        return document



    def get_values_db_ref_from_list(self, list: list) -> list:
        """
        Mongo -> Py
        """
        processed_list = []
        collection_ref = self.data_base[list[0]._id.collection]
        for item in list:
            _id = ObjectId(item._id)
            document_ref = collection_ref.find_one({'_id':_id})
            document_ref['_id'] = document_ref['_id'].__str__()
            processed_list.append(document_ref)
        return processed_list


    def transform_object_ids(self, document: dict) -> dict:
        """
        This method transform sub-documents
        Mongo -> Py
        """
        for key in document.keys():
            value = document.get(key)
            if isinstance(value, ObjectId):
                document[key] = document[key].__str__()
            elif isinstance(value, list) and len(list) > 0:
                document[key] = self.format_list(value)
            elif isinstance(value, dict):
                document[key] = self.transform_object_ids(value)
        return document

    def transform_refs(self, item: T) -> T:
        """
        Py -> Mongo
        :return:
        """
        item_dict = item.__dict__
        for key in item_dict.keys():
            if item_dict.get(key).__str__().count("object") == 1:
                object_ = self.object_to_db_ref(getattr(item, key))
                setattr(item, key, object_)
        return item

#==========SPRINT 2 ==========
    #TODO: merge with find_all
    def query(self, query: dict) -> list:
        """
        This method make filtered queries
        """
        dataset = []
        for document in self.current_collection.find(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    # TODO: create a function to format the query
    def query_aggregation(self, query: dict) -> list:
        """
        Pylint: queries generated by the database
        """
        dataset = []
        for document in self.current_collection.aggregate(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def format_list(self, list: list) -> list:
        """
        Mongo -> Py
        """
        processed_list = []
        for item in list:
            if isinstance(item, ObjectId):
                temp = item.__str__()
                processed_list.append(temp)
        if not processed_list:
            processed_list =  list
        return processed_list

    def object_to_db_ref(self, object_ref) -> DBRef:
        """
        This method format a list of values, similar to toString() in Java
        Py -> Mongo
        """
        collection_ref = object_ref.__class__.__name__.lower()
        return DBRef(collection_ref, ObjectId(object_ref._id))
