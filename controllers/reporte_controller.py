from repositories.reporte_repository import ReportsRepository

class ReportsController():
    def __init__(self) -> None:
        print("Reports controller ready...")
        self.reports_repository = ReportsRepository()
    
    def get_sorted_candidato(self) -> list:
        print("Get candidatos from all mesas sorted desc by the enrollments amount.")
        return self.reports_repository.get_sorted_candidato()
    
    def get_sorted_candidato_by_mesa(self, mesa_id: str) -> list:
        print("Get sorted candidatos from a given mesa.")
        return self.reports_repository.get_sorted_candidato_by_mesa(mesa_id)
    
    def get_sorted_partido(self) -> list:
        return self.reports_repository.get_sorted_partido()
    
    def get_sorted_partido_by_mesa(self, mesa_id: str) -> list:
        return self.reports_repository.get_sorted_partido_by_mesa(mesa_id)

    def get_sorted_mesa(self) -> list:
        return self.reports_repository.get_sorted_mesa()

    def get_porcentual_partido(self) -> list:
        return self.reports_repository.get_porcentual_partidos()