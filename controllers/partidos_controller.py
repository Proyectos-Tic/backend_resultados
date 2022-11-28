from models.partidos import Partidos
from repositories.partidos_repository import PartidosRepository
class PartidosController():

    def __init__(self) -> None:
        print("Partidos controller ready...")
        self.partidos_repository = PartidosRepository()
    
    def index(self) -> list:
        """
        This method returns a list of all parties

        :return: list
        """
        return self.partidos_repository.find_all()
    
    def show(self, id: str) -> dict:
        """
        This method returns a party by id

        :param id: str
        :return: dict
        """
        return self.partidos_repository.find_by_id(id)
    
    def create(self, party: dict) -> dict:
        """
        This method creates a party

        :param party: dict
        :return: dict
        """
        party_ = Partidos(party)
        return self.partidos_repository.save(party_)
    
    def update(self, id: str, party: dict) -> dict:
        """
        This method updates a party by id

        :param id: str
        :param party: dict
        :return: dict
        """
        party_ = Partidos(party)
        return self.partidos_repository.update(id, party_)
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a party by id

        :param id: str
        :return: dict
        """
        return self.partidos_repository.delete(id)
    