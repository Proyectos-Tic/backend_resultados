from models.candidate import Candidate
from models.party import Party
from repositories.party_repository import PartyRepository
from repositories.candidate_repository import CandidateRepository


class CandidateController:

    def __init__(self):
        self.candidate_repository = CandidateRepository()
        self.party_repository = PartyRepository()

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

    def party_assign(self, candidate_id: str, party_id: str) -> dict:
        """
        Assign this instance of candidate to an existing party providing the party ID

        :param candidate_id:
        :param party_id:
        :return:
        """
        party_dict = self.party_repository.find_by_id(party_id)
        party_obj = Party(party_dict)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)

        candidate_obj.party = party_obj
        return self.candidate_repository.save(candidate_obj)

