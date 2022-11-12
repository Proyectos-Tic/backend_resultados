from bson import ObjectId

from models.result import Result
from repositories.interfaceRepository import InterfaceRepository


class ResultRepository(InterfaceRepository[Result]):

    def get_report_by_candidate(self, candidate_id: str) -> list:
        query_dict = {"candidate.$id": ObjectId(candidate_id)}
        return self.query(query_dict)

    def get_report_by_table(self, table_id: str) -> list:
        table_query = {"$match": {"table.$id": ObjectId(table_id)}}
        group_query = {"$group": {"_id": "$candidate.$id", "count": {"$sum": 1}}}
        pipeline = [table_query, group_query]
        return self.query_aggregation(pipeline)

    def get_general_result_counts(self):
        query_aggregation = {"$group": {"_id": "$candidate.$id", "count": {"$sum": 1}}}
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_table_participation(self):
        query_aggregation = {"$group": {"_id": "$table.$id", "count": {"$sum": 1}}}
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_party_votes(self):
        query_aggregation = {"$group": {"_id": "$party.$id", "count": {"$sum": 1}}}
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)
