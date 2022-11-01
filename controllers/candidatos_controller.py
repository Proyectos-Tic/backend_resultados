from models.candidatos import Candidatos

class CandidatosController():

    def __init__(self) -> None:
        print("Candidatos controller ready...")

    def index(self) -> list:
        """
        This method returns a list of all candidates

        :return: list
        """
        print("Get all candidates")
        candidate = {
            "n_resolution": "123",
            "id_personal": "101015",
            "name": "John",
            "lastname": "Doe",
            "pol_party": "PAN",
        }
        return [candidate]

    def show(self, id: str) -> dict:
        """
        This method returns a candidate by id

        :param id: str
        :return: dict
        """
        print("Get candidate by id")
        candidate = {
            "n_resolution": "456",
            "id_personal": id,
            "name": "Carl",
            "lastname": "Johnson",
            "pol_party": "GLP",
        }
        return candidate


    
    def create(self, candidate: dict) -> dict:
        """
        This method creates a candidate

        :param candidate: dict
        :return: dict
        """
        print("Create candidate: ", end="")
        print(candidate)

        candidate_ = Candidatos(candidate)
        return candidate_.__dict__

    
    def update(self, id: str, candidate: dict) -> dict:
        """
        This method updates a candidate by id

        :param id: str
        :param candidate: dict
        :return: dict
        """
        print("Update candidate")
        candidate["id_personal"] = id
        candidate_ = Candidatos(candidate)
        return candidate_.__dict__
    
    def delete(self, id: str) -> dict:
        """
        This method deletes a candidate by id

        :param id: str
        :return: dict
        """
        print("Delete candidate")
        deleted_candidate = {
            'Message': f'Candidate with id {id} was deleted',
        }
        return deleted_candidate