from abc import ABCMeta

class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict) -> dict:
        """
        This method is a constructor where a dict is passed as a parameter

        :param data: dict
        :return: dict
        """
        for key, value in data.items():
            setattr(self, key, value)