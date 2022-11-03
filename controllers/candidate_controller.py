

class CandidateController:

    def __init__(self):
        print("Candidate controller constructor")

    def index(self) -> list:
        """
        Get all candidates

        :return:
        """
        print("Get all candidates")

    def show(self, id_: str) -> dict:
        """
        Get a specific candidate providing its id

        :param id_:
        :return:
        """
        print("Get a specific candidate providing its id")

    def create(self, candidate_: dict) -> dict:
        """
        Create a new candidate

        :param candidate_:
        :return:
        """
        print("Create a new candidate")

    def update(self, id_: str, candidate_: dict) -> dict:
        """
        Modify an existing candidate

        :param id_:
        :param candidate_:
        :return:
        """
        print("Modify an existing candidate")

    def delete(self, id_: str) -> str:
        """
        Delete a candidate providing its id

        :param id_:
        :return:
        """
        print("Delete a candidate providing its id")
