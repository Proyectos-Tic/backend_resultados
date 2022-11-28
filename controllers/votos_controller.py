from models.votos import Votos
from repositories.votos_repository import VotosRepository

from models.mesas import Mesas
from models.candidatos import Candidatos
from repositories.mesas_repository import MesasRepository
from repositories.candidatos_repository import CandidatosRepository

class VotosController():

    def __init__(self) -> None:
        print("Votos controller ready...")
        self.votos_repository = VotosRepository()
        self.mesas_repository = MesasRepository()
        self.candidatos_repository = CandidatosRepository()
    
    def index(self) -> list:
        """
        This method returns a list of all votes
        :return: list
        """
        return self.votos_repository.find_all()
    
    def show(self, id: str) -> dict:
        """
        This method returns a vote by id
        :param id: str
        :return: dict
        """
        return self.votos_repository.find_by_id(id)
    
    def create(self, mesa_id: str, candidato_id: str) -> dict:
        """
        This method creates a vote
        :param vote: dict
        :return: dict
        """
        vote_ = Votos({})
        mesa_dict = self.mesas_repository.find_by_id(mesa_id)
        mesa_obj = Mesas(mesa_dict)
        candidato_dict = self.candidatos_repository.find_by_id(candidato_id)
        candidato_obj = Candidatos(candidato_dict)
        vote_.mesa = mesa_obj
        vote_.candidato = candidato_obj
        return self.votos_repository.save(vote_)
    
    def update(self, id: str, vote: dict) -> dict:
        """
        This method updates a vote by id
        :param id: str
        :param vote: dict
        :return: dict
        """
        vote_ = Votos(vote)
        return self.votos_repository.update(id, vote_)
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a vote by id
        :param id: str
        :return: dict
        """
        return self.votos_repository.delete(id)
    
    