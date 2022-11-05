from models.candidate import Candidate
from repositories.candidate_repository import CandidateRepository


class CandidateController:

    def __init__(self):
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        """
        Get all candidates

        :return:
        """
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        Get a specific candidate providing its id

        :param id_:
        :return:
        """
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """
        Create a new candidate

        :param candidate_:
        :return:
        """
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, id_: str, candidate_: dict) -> dict:
        """
        Modify an existing candidate

        :param id_:
        :param candidate_:
        :return:
        """
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)

    def delete(self, id_: str) -> dict:
        """
        Delete a candidate providing its id

        :param id_:
        :return:
        """
        return self.candidate_repository.delete(id_)
