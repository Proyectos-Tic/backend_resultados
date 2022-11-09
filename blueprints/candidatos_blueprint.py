from flask import Blueprint, request

from controllers.candidatos_controller import CandidatosController

candidatos_blueprint = Blueprint('candidatos_blueprint', __name__)
candidatos_controller = CandidatosController()

@candidatos_blueprint.route("/candidato/all", methods=["GET"])
def get_all_candidates():
    response = candidatos_controller.index()
    return response, 200

@candidatos_blueprint.route("/candidato/<string:id>", methods=["GET"])
def get_candidate_by_id(id):
    response = candidatos_controller.show(id)
    return response, 200

@candidatos_blueprint.route("/candidato/create", methods=["POST"])
def create_candidate():
    candidate = request.get_json()
    response = candidatos_controller.create(candidate)
    return response, 201

@candidatos_blueprint.route("/candidato/update/<string:id>", methods=["PATCH"])
def update_candidate(id):
    candidate = request.get_json()
    response = candidatos_controller.update(id, candidate)
    return response, 201

@candidatos_blueprint.route('/candidato/<string:candidate_id>/partido/<string:party_id>', methods=['PUT'])
def assign_candidate(candidate_id, party_id):
    response = candidatos_controller.assign_party(candidate_id, party_id)
    return response, 201

@candidatos_blueprint.route("/candidato/delete/<string:id>", methods=["DELETE"])
def delete_candidate(id):
    response = candidatos_controller.delete(id)
    return response, 200
