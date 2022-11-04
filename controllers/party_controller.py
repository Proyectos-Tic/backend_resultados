from models.party import Party
from repositories.party_repository import PartyRepository


class PartyController:

    def __init__(self):
        self.party_repository = PartyRepository()

    def index(self) -> list:
        """
        Get all parites

        :return:
        """
        return self.party_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        Get a specific party providing the id

        :param id_:
        :return:
        """
        return self.party_repository.find_by_id(id_)

    def create(self, party_: dict) -> dict:
        """
        Create a new party

        :param party_:
        :return:
        """
        party = Party(party_)
        return self.party_repository.save(party)

    def update(self, id_: str, party_: dict) -> dict:
        """
        Modify an existing party

        :param id_:
        :param party_:
        :return:
        """
        party = Party(party_)
        return self.party_repository.update(id_, party)

    def delete(self, id_: str) -> dict:
        """
        Delete a party providing its id
        
        :param id_:
        :return:
        """
        return self.party_repository.delete(id_)
