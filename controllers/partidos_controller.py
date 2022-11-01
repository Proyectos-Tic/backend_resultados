
class PartidosController():

    def __init__(self) -> None:
        print("Partidos controller ready...")
    
    def index(self) -> list:
        """
        This method returns a list of all parties

        :return: list
        """
        print("Get all parties")
    
    def show(self, id: str) -> dict:
        """
        This method returns a party by id

        :param id: str
        :return: dict
        """
        print("Get party by id")
    
    def create(self, party: dict) -> dict:
        """
        This method creates a party

        :param party: dict
        :return: dict
        """
        print("Create party")
    
    def update(self, id: str, party: dict) -> dict:
        """
        This method updates a party by id

        :param id: str
        :param party: dict
        :return: dict
        """
        print("Update party")
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a party by id

        :param id: str
        :return: dict
        """
        print("Delete party")
    