from models.mesas import Mesas
from repositories.mesas_repository import MesasRepository

class MesasController():
    
    def __init__(self) -> None:
        print("Mesas controller ready...")
        self.mesas_repository = MesasRepository()

    def index(self) -> list:
        """
        This method returns a list of all tables
        :return: list
        """
        print("Get all tables")
        return self.mesas_repository.find_all()
    
    def show(self, id: str) -> dict:
        """
        This method returns a table by id
        :param id: str
        :return: dict
        """
        print("Get table by id")
        return self.mesas_repository.find_by_id(id)
    
    def create(self, table: dict) -> dict:
        """
        This method creates a table
        :param table: dict
        :return: dict
        """
        print("Create table")
        table_ = Mesas(table)
        return self.mesas_repository.save(table_)
    
    def update(self, id: str, table: dict) -> dict:
        """
        This method updates a table by id
        :param id: str
        :param table: dict
        :return: dict
        """
        print("Update table")
        table_ = Mesas(table)
        return self.mesas_repository.update(id, table_)
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a table by id
        :param id: str
        :return: dict
        """
        print("Delete table")
        return self.mesas_repository.delete(id)