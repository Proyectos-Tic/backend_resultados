from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        """
        Constructor method that parses a dictionary into an object.

        :param data:
        """
        for key, value in data.items():
            setattr(self, key, value)
