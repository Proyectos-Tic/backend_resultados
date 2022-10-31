

class CandidatosController():

    def __init__(self) -> None:
        print("Candidatos controller ready...")

    def index(self) -> list:
        """
        This method returns a list of all candidates

        :return: list
        """
        print("Get all candidates")

    def show(self, id: int) -> dict:
        """
        This method returns a candidate by id

        :param id: int
        :return: dict
        """
        print("Get candidate by id")
    
    def create(self, candidate: dict) -> dict:
        """
        This method creates a candidate

        :param candidate: dict
        :return: dict
        """
        print("Create candidate")
    
    def update(self, id: int, candidate: dict) -> dict:
        """
        This method updates a candidate by id

        :param id: int
        :param candidate: dict
        :return: dict
        """
        print("Update candidate")
    
    def delete(self, id: int) -> dict:
        """
        This method deletes a candidate by id

        :param id: int
        :return: dict
        """
        print("Delete candidate")