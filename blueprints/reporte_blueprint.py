from flask import Blueprint
from flask import request

from controllers.reporte_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()

@reports_blueprints.route("/reports/voto/sorted_candidato", methods=["GET"])
def report_sorted_candidato():
    response = reports_controller.get_sorted_candidato()
    return response, 200

@reports_blueprints.route('/reports/voto/sorted_candidato/<string:mesa_id>', methods=["GET"])
def report_sorted_candidato_by_mesa(mesa_id):
    response = reports_controller.get_sorted_candidato_by_mesa(mesa_id)
    return response, 200

@reports_blueprints.route('/reports/voto/sorted_partido', methods=["GET"])
def report_sorted_partido():
    response = reports_controller.get_sorted_partido()
    return response, 200

@reports_blueprints.route('/reports/voto/sorted_partido/<string:mesa_id>', methods=["GET"])
def report_sorted_partido_by_mesa(mesa_id: str):
    response = reports_controller.get_sorted_partido_by_mesa(mesa_id)
    return response, 200

@reports_blueprints.route('/reports/voto/sorted_mesa', methods=["GET"])
def report_sorted_mesa():
    response = reports_controller.get_sorted_mesa()
    return response, 200

@reports_blueprints.route('/reports/voto/partido/porcentual', methods=["GET"])
def report_sorted_partido_porcentual():
    response = reports_controller.get_porcentual_partido()
    return response, 200