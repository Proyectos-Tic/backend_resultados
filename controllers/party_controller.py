

class PartyController:

    def __init__(self):
        print("Party controller constructor")

    def index(self) -> list:
        """
        Get all parites

        :return:
        """
        print("Get all parties")

    def show(self, id_: str) -> dict:
        """
        Get a specific party providing the id

        :param id_:
        :return:
        """
        print("Get a specific party provided the id")

    def create(self, party_: dict) -> dict:
        """
        Create a new party

        :param party_:
        :return:
        """
        print("Create a new party")

    def update(self, id_: str, party_: dict) -> dict:
        """
        Modify an existing party

        :param id_:
        :param party_:
        :return:
        """
        print("Modify an existing party")

    def delete(self, id_: str) -> str:
        """
        Delete a party providing its id
        
        :param id_:
        :return:
        """
        print("Delete a party providing its id")
