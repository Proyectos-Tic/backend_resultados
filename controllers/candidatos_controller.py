from models.candidatos import Candidatos
from repositories.candidatos_repository import CandidatosRepository

class CandidatosController():

    def __init__(self) -> None:
        print("Candidatos controller ready...")
        self.candidatos_repository = CandidatosRepository()

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
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a candidate by id

        :param id: str
        :return: dict
        """
        print("Delete candidate")
        return self.candidatos_repository.delete(id)