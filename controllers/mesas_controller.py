
class MesasController():
    
    def __init__(self) -> None:
        print("Mesas controller ready...")

    def index(self) -> list:
        """
        This method returns a list of all tables
        :return: list
        """
        print("Get all tables")
    
    def show(self, id: str) -> dict:
        """
        This method returns a table by id
        :param id: str
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
    
    def update(self, id: str, table: dict) -> dict:
        """
        This method updates a table by id
        :param id: str
        :param table: dict
        :return: dict
        """
        print("Update table")
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a table by id
        :param id: str
        :return: dict
        """
        print("Delete table")