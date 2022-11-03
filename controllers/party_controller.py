

class PartyController:

    def __init__(self):
        print("Party controller constructor")

    def index(self) -> list:
        print("Get all parties")

    def show(self, id_: str) -> dict:
        print("Get a specific party provided the id")

    def create(self, party_: dict) -> dict:
        print("Create a new party")

    def update(self, id_: str, party_: dict) -> dict:
        print("Modify an existing party")

    def delete(self, id_: str) -> str:
        print("Delete a party providing its id")