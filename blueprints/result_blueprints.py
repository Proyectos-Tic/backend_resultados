from flask import Blueprint, request
from controllers.result_controller import ResultController

result_blueprints = Blueprint('result_blueprint', __name__)
result_controller = ResultController()


@result_blueprints.route("result/insert", methods=['POST'])
def insert_result():
    result = request.get_json()
    response = result_controller.create(result)
    return response, 201
