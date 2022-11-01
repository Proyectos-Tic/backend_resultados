

class CandidatosController():

    def __init__(self) -> None:
        print("Candidatos controller ready...")

    def index(self) -> list:
        """
        This method returns a list of all candidates

        :return: list
        """
        print("Get all candidates")

    def show(self, id: str) -> dict:
        """
        This method returns a candidate by id

        :param id: str
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
    
    def update(self, id: str, candidate: dict) -> dict:
        """
        This method updates a candidate by id

        :param id: str
        :param candidate: dict
        :return: dict
        """
        print("Update candidate")
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a candidate by id

        :param id: str
        :return: dict
        """
        print("Delete candidate")