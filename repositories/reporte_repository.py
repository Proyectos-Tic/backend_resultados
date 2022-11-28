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
        pipeline = [
            {
                '$lookup': {
                    'from': 'candidatos', 
                    'localField': 'candidato.$id', 
                    'foreignField': '_id', 
                    'as': 'result'
                }
            }, {
                '$unwind': '$result'
            }, {
                '$addFields': {
                    'partido': '$result.partido'
                }
            }, {
                '$project': {
                    'partido': 1, 
                    '_id': 1
                }
            }, {
                '$lookup': {
                    'from': 'partidos', 
                    'localField': 'partido.$id', 
                    'foreignField': '_id', 
                    'as': 'partidos'
                }
            }, {
                '$unwind': {
                    'path': '$partidos'
                }
            }, {
                '$group': {
                    '_id': '$partidos._id', 
                    'Votos_partido': {
                        '$sum': 1
                    }, 
                    'partidos': {
                        '$first': '$partidos'
                    }
                }
            }, {
                '$addFields': {
                    'nombre': '$partidos.nombre'
                }
            }, {
                '$sort': {
                    'Votos_partido': -1
                }
            }, {
                '$project': {
                    '_id': 1, 
                    'Votos_partido': 1, 
                    'nombre': 1
                }
            }
        ]
        return self.query_aggregation(pipeline)

    def get_sorted_partido_by_mesa(self, mesa_id: str) -> list:
        pipeline = [
            {
                '$match': {
                    'mesa.$id': ObjectId(mesa_id)
                }
            }, {
                '$lookup': {
                    'from': 'candidatos', 
                    'localField': 'candidato.$id', 
                    'foreignField': '_id', 
                    'as': 'result'
                }
            }, {
                '$unwind': '$result'
            }, {
                '$addFields': {
                    'partido': '$result.partido'
                }
            }, {
                '$project': {
                    'partido': 1, 
                    '_id': 1
                }
            }, {
                '$lookup': {
                    'from': 'partidos', 
                    'localField': 'partido.$id', 
                    'foreignField': '_id', 
                    'as': 'partidos'
                }
            }, {
                '$unwind': {
                    'path': '$partidos'
                }
            }, {
                '$group': {
                    '_id': '$partidos._id', 
                    'Votos_partido': {
                        '$sum': 1
                    }, 
                    'partidos': {
                        '$first': '$partidos'
                    }
                }
            }, {
                '$addFields': {
                    'nombre': '$partidos.nombre'
                }
            }, {
                '$sort': {
                    'Votos_partido': -1
                }
            }, {
                '$project': {
                    '_id': 1, 
                    'Votos_partido': 1, 
                    'nombre': 1
                }
            }
        ]
        print(self.query_aggregation(pipeline))
        return self.query_aggregation(pipeline)

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
        pipeline = [
                {
                    '$group': {
                        '_id': '$candidato.$id', 
                        'Votos_candidato': {
                            '$count': {}
                        }, 
                        'candidato': {
                            '$first': '$candidato'
                        }
                    }
                }, {
                    '$sort': {
                        'Votos_candidato': -1
                    }
                }, {
                    '$limit': 15
                }, {
                    '$lookup': {
                        'from': 'candidatos', 
                        'localField': 'candidato.$id', 
                        'foreignField': '_id', 
                        'as': 'result'
                    }
                }, {
                    '$unwind': {
                        'path': '$result'
                    }
                }, {
                    '$addFields': {
                        'partido': '$result.partido'
                    }
                }, {
                    '$lookup': {
                        'from': 'partidos', 
                        'localField': 'partido.$id', 
                        'foreignField': '_id', 
                        'as': 'partidos'
                    }
                }, {
                    '$unwind': {
                        'path': '$partidos'
                    }
                }, {
                    '$group': {
                        '_id': '$partidos._id', 
                        'Total_partido': {
                            '$sum': 1
                        }
                    }
                }, {
                    '$project': {
                        '_id': 1, 
                        'Total_partido': 1, 
                        'Porcentaje': {
                            '$round': [
                                {
                                    '$multiply': [
                                        {
                                            '$divide': [
                                                '$Total_partido', 15
                                            ]
                                        }, 100
                                    ]
                                }, 1
                            ]
                        }
                    }
                },{
                    '$sort': {
                        'Porcentaje': -1
                    }
                }
            ]
        return self.query_aggregation(pipeline)