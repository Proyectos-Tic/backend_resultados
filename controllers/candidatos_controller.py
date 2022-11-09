from models.candidatos import Candidatos
from repositories.candidatos_repository import CandidatosRepository

from models.partidos import Partidos
from repositories.partidos_repository import PartidosRepository

class CandidatosController():

    def __init__(self) -> None:
        print("Candidatos controller ready...")
        self.candidatos_repository = CandidatosRepository()
        self.partidos_repository = PartidosRepository()

    def index(self) -> list:
        """
        This method returns a list of all candidates

        :return: list
        """
        print("Get all candidates")
        return self.candidatos_repository.find_all()

    def show(self, id: str) -> dict:
        """
        This method returns a candidate by id

        :param id: str
        :return: dict
        """
        print("Get candidate by id")
        return self.candidatos_repository.find_by_id(id)


    
    def create(self, candidate: dict) -> dict:
        """
        This method creates a candidate

        :param candidate: dict
        :return: dict
        """
        print("Create candidate: ", end="")
        print(candidate)

        candidate_ = Candidatos(candidate)
        return self.candidatos_repository.save(candidate_)

    
    def update(self, id: str, candidate: dict) -> dict:
        """
        This method updates a candidate by id

        :param id: str
        :param candidate: dict
        :return: dict
        """
        print("Update candidate")
        candidate_ = Candidatos(candidate)
        return self.candidatos_repository.update(id,candidate_)

    def assign_party(self, candidate_id: str, party_id: str) -> dict:
        """
        
        """
        candidate_dict = self.candidatos_repository.find_by_id(candidate_id)
        candidate_obj = Candidatos(candidate_dict)
        party_dict = self.partidos_repository.find_by_id(party_id)
        party_obj = Partidos(party_dict)
        candidate_obj.partido = party_obj
        return self.candidatos_repository.save(candidate_obj)
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a candidate by id

        :param id: str
        :return: dict
        """
        print("Delete candidate")
        return self.candidatos_repository.delete(id)