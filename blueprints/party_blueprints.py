from flask import Blueprint, request

from controllers.party_controller import PartyController

party_blueprints = Blueprint('party_blueprints', __name__)
party_controller = PartyController()


@party_blueprints.route("/party/all", methods=['GET'])
def get_all_parties():
    response = party_controller.index()
    return response, 200


@party_blueprints.route("/party/<string:id_>", methods=['GET'])
def get_party_by_id(id_):
    response = party_controller.show(id_)
    return response, 200


@party_blueprints.route("/party/insert", methods=['POST'])
def insert_party():
    party = request.get_json()
    response = party_controller.create(party)
    return response, 201


@party_blueprints.route("/party/update/<string:id_>", methods=['PATCH'])
def update_party(id_):
    party = request.get_json()
    response = party_controller.update(id_, party)
    return response, 201


@party_blueprints.route("/party/delete/<string:id_>", methods=['DELETE'])
def delete_party(id_):
    response = party_controller.delete(id_)
    return response, 204
