from flask import Blueprint, request
from controllers.result_controller import ResultController


result_blueprints = Blueprint('result_blueprint', __name__)
result_controller = ResultController()


@result_blueprints.route("/result/table/<string:table_id>/candidate/<string:candidate_id>", methods=['POST'])
def insert_result(table_id, candidate_id):
    result = request.get_json()
    response = result_controller.create(result, table_id, candidate_id)
    return response, 201


@result_blueprints.route("/reports/candidate/<string:candidate_id>", methods=['GET'])
def report_results_by_candidate(candidate_id):
    response = result_controller.get_results_by_candidate(candidate_id)
    return response, 200


@result_blueprints.route("/reports/table/<string:table_id>", methods=['GET'])
def report_results_by_table(table_id):
    response = result_controller.get_results_by_table(table_id)
    return response, 200


@result_blueprints.route("/reports/general", methods=['GET'])
def report_general_results():
    response = result_controller.get_general_results()
    return response, 200


@result_blueprints.route("/reports/table_participation", methods=['GET'])
def report_table_participation():
    response = result_controller.get_table_participation()
    return response, 200


@result_blueprints.route("/reports/parties", methods=['GET'])
def report_party_votes():
    response = result_controller.get_party_votes()
    return response, 200
