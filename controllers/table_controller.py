

class TableController:

    def __init__(self):
        print("Table Controller Constructor")

    def index(self) -> list:
        """
        Get all tables

        :return:
        """
        print("Get all tables")

    def show(self, id_: str) -> dict:
        """
        Get a specific table given its id

        :param id_:
        :return:
        """
        print("Get a specific table given its id")

    def create(self, table_: dict) -> dict:
        """
        Create a new table

        :param table_:
        :return:
        """
        print("Create a new table")

    def update(self, id_: str, table_: dict) -> dict:
        """
        Modify an existing table

        :param id_:
        :param table_:
        :return:
        """
        print("Modify an existing table")

    def delete(self, id_: str) -> str:
        """
        Delete a table providing its id

        :param id_:
        :return:
        """
        print("Delete a table providing its id")
