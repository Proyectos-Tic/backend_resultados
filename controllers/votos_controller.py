from models.votos import Votos
from repositories.votos_repository import VotosRepository

class VotosController():

    def __init__(self) -> None:
        print("Votos controller ready...")
        self.votos_repository = VotosRepository()
    
    def index(self) -> list:
        """
        This method returns a list of all votes
        :return: list
        """
        print("Get all votes")
        return self.votos_repository.find_all()
    
    def show(self, id: str) -> dict:
        """
        This method returns a vote by id
        :param id: str
        :return: dict
        """
        print("Get vote by id")
        return self.votos_repository.find_by_id(id)
    
    def create(self, vote: dict) -> dict:
        """
        This method creates a vote
        :param vote: dict
        :return: dict
        """
        print("Create vote")
        vote_ = Votos(vote)
        return self.votos_repository.save(vote_)
    
    def update(self, id: str, vote: dict) -> dict:
        """
        This method updates a vote by id
        :param id: str
        :param vote: dict
        :return: dict
        """
        print("Update vote")
        vote_ = Votos(vote)
        return self.votos_repository.update(id, vote_)
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a vote by id
        :param id: str
        :return: dict
        """
        print("Delete vote")
        return self.votos_repository.delete(id)
    
    