from models.result import Result
from repositories.result_repository import ResultRespository


class ResultController:

    def __init__(self):
        self.result_repository = ResultRespository()

    def create(self, result_:dict) -> dict:
        """
        Create a new vote

        :param result_:
        :return:
        """
        result = Result(result_)
        return self.result_repository(result)

