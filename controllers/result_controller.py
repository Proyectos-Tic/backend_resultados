from models.result import Result
from models.candidate import Candidate
from models.table import Table
from repositories.candidate_repository import CandidateRepository
from repositories.table_repository import TableRepository
from repositories.result_repository import ResultRepository


class ResultController:

    def __init__(self):
        self.result_repository = ResultRepository()
        self.candidate_repository = CandidateRepository()
        self.table_repository = TableRepository()

    def create(self, result_: dict, table_id: str, candidate_id: str) -> dict:
        """
        Create a new vote providing table ID and candidate ID through the URL of the request.

        :param result_:
        :param table_id:
        :param candidate_id:
        :return:
        """
        vote = Result(result_)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)

        vote.table = table_obj
        vote.candidate = candidate_obj
        return self.result_repository.save(vote)

    def get_results_by_candidate(self, candidate_id: str) -> list:
        """
        Get a list of votes for a specific candidate.

        :param candidate_id:
        :return:
        """
        return self.result_repository.get_report_by_candidate(candidate_id)

    def get_results_by_table(self, table_id: str) -> list:
        """
        Get a list of votes for a specific table.

        :param table_id:
        :return:
        """
        return self.result_repository.get_report_by_table(table_id)

    def get_general_results(self):
        """
        Get a general vote count from all candidates and tables

        :return:
        """
        results_list = self.result_repository.get_general_result_counts()
        for candidate in results_list:
            candidate_info = self.candidate_repository.find_by_id(candidate.get('_id'))
            del candidate['_id']
            candidate.update({'candidate': candidate_info})
        return results_list

    def get_table_participation(self):
        """
        Get a count of votes per table

        :return:
        """
        participation_list = self.result_repository.get_table_participation()
        for table in participation_list:
            table_info = self.table_repository.find_by_id(table.get('_id'))
            del table['_id']
            table.update({'table': table_info})
        return participation_list
