from flask import Blueprint, request

from controllers.partidos_controller import PartidosController

partidos_blueprint = Blueprint('partidos_blueprint', __name__)
partidos_controller = PartidosController()

@partidos_blueprint.route("/partido/all", methods=["GET"])
def get_all_parties():
    response = partidos_controller.index()
    return response, 200

@partidos_blueprint.route("/partido/<string:id>", methods=["GET"])
def get_party_by_id(id):
    response = partidos_controller.show(id)
    return response, 200

@partidos_blueprint.route("/partido/create", methods=["POST"])
def create_party():
    party = request.get_json()
    response = partidos_controller.create(party)
    return response, 200

@partidos_blueprint.route("/partido/update/<string:id>", methods=["PATCH"])
def update_party(id):
    party = request.get_json()
    response = partidos_controller.update(id, party)
    return response, 200

@partidos_blueprint.route("/partido/delete/<string:id>", methods=["DELETE"])
def delete_party(id):
    response = partidos_controller.delete(id)
    return response, 200