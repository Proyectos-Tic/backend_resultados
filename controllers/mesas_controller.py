
class MesasController():
    
    def __init__(self) -> None:
        print("Mesas controller ready...")

    def index(self) -> list:
        """
        This method returns a list of all tables
        :return: list
        """
        print("Get all tables")
    
    def show(self, id: int) -> dict:
        """
        This method returns a table by id
        :param id: int
        :return: dict
        """
        print("Get table by id")
    
    def create(self, table: dict) -> dict:
        """
        This method creates a table
        :param table: dict
        :return: dict
        """
        print("Create table")
    
    def update(self, id: int, table: dict) -> dict:
        """
        This method updates a table by id
        :param id: int
        :param table: dict
        :return: dict
        """
        print("Update table")
    
    def delete(self, id: int) -> dict:
        """
        This method deletes a table by id
        :param id: int
        :return: dict
        """
        print("Delete table")