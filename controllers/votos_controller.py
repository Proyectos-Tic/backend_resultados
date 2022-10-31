

class VotosController():

    def __init__(self) -> None:
        print("Votos controller ready...")
    
    def index(self) -> list:
        """
        This method returns a list of all votes
        :return: list
        """
        print("Get all votes")
    
    def show(self, id: int) -> dict:
        """
        This method returns a vote by id
        :param id: int
        :return: dict
        """
        print("Get vote by id")
    
    def create(self, vote: dict) -> dict:
        """
        This method creates a vote
        :param vote: dict
        :return: dict
        """
        print("Create vote")
    
    def update(self, id: int, vote: dict) -> dict:
        """
        This method updates a vote by id
        :param id: int
        :param vote: dict
        :return: dict
        """
        print("Update vote")
    
    def delete(self, id: int) -> dict:
        """
        This method deletes a vote by id
        :param id: int
        :return: dict
        """
        print("Delete vote")
    
    