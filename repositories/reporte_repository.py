from bson import ObjectId
from repositories.interfaceRepository import InterfaceRepository
from models.votos import Votos

class ReportsRepository(InterfaceRepository[Votos]):
    
    def get_report_value(self, response: list, sub_dict: str, sub_dict_name: str) -> list:
        new_response = []
        for dataset in response:
            if sub_dict in dataset:
                new_dict = {}
                new_dict["_id"] = dataset["_id"]
                new_dict[sub_dict] = {"_id": dataset[sub_dict].get("_id"), sub_dict_name: dataset[sub_dict].get(sub_dict_name)}
                print("Nuevo dict:"+str(new_dict))
                new_response.append(new_dict)
                print(new_response)
        return new_response

    def get_sorted_candidato(self) -> list:
        query_group = {
                '$group': {
                    '_id': '$candidato.$id', 
                    'candidato': {
                        '$first': '$candidato'
                    }, 
                    'count': {
                        '$count': {}
                    }
                }
            }
        query_sort = {
                '$sort': {
                    'count': -1
                }
            }
            
        pipeline = [query_group,query_sort]
        return self.query_aggregation(pipeline)
    
    def get_sorted_candidato_by_mesa(self, mesa_id: str) -> list:
        query_match = {
                '$match': {
                    'mesa.$id': ObjectId(mesa_id)
                }
        }
        query_group = {
                '$group': {
                    '_id': '$candidato.$id', 
                    'candidato': {
                        '$first': '$candidato'
                    }, 
                    'count': {
                        '$count': {}
                    }
                }
        }
        query_sort = {
                '$sort': {
                    'count': -1
                }
        }
        
        pipeline = [query_match,query_group,query_sort]
        return self.query_aggregation(pipeline)

    def get_sorted_partido(self) -> list:
        return ['Get sorted partidos']

    def get_sorted_partido_by_mesa(self, mesa_id: str) -> list:
        return ['Get sorted partidos by mesa']

    def get_sorted_mesa(self) -> list:
        query_group = {
                '$group': {
                    '_id': '$mesa.$id', 
                    'count': {
                        '$count': {}
                    }, 
                    'mesa': {
                        '$first': '$mesa'
                    }
                }
            }
        query_sort = {
                '$sort': {
                    'mesa': -1
                }
            }
        
        pipeline = [query_group, query_sort]
        return self.query_aggregation(pipeline)

    def get_porcentual_partidos(self) -> list:
        return ['Get sorted porcentual partidos'] 