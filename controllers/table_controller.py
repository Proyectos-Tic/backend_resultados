from models.table import Table
from repositories.table_repository import TableRepository


class TableController:

    def __init__(self):
        self.table_repository = TableRepository()

    def index(self) -> list:
        """
        Get all tables

        :return:
        """
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        Get a specific table given its id

        :param id_:
        :return:
        """
        return self.table_repository.find_by_id(id_)

    def create(self, table_: dict) -> dict:
        """
        Create a new table

        :param table_:
        :return:
        """
        table = Table(table_)
        return self.table_repository.save(table)

    def update(self, id_: str, table_: dict) -> dict:
        """
        Modify an existing table

        :param id_:
        :param table_:
        :return:
        """
        table = Table(table_)
        return self.table_repository.update(id_, table)

    def delete(self, id_: str) -> dict:
        """
        Delete a table providing its id

        :param id_:
        :return:
        """
        return self.table_repository.delete(id_)
