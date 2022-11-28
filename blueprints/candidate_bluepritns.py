from flask import Blueprint, request

from controllers.candidate_controller import CandidateController

candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()


@candidate_blueprints.route("/candidate/all", methods=['GET'])
def get_all_candidates():
    response = candidate_controller.index()
    return response, 200


@candidate_blueprints.route("/candidate/<string:id_>", methods=['GET'])
def get_candidate_by_id(id_):
    response = candidate_controller.show(id_)
    return response, 200


@candidate_blueprints.route("/candidate/insert", methods=['POST'])
def insert_candidate():
    candidate = request.get_json()
    creation_response = candidate_controller.create(candidate)
    candidate_id = creation_response['_id'];
    party_id = creation_response['party']['_id']
    print(f'CANDIDATE ID = {candidate_id}')
    print(f'PARTY ID = {party_id}')
    response = candidate_controller.party_assign(candidate_id, party_id);
    return response, 201


@candidate_blueprints.route("/candidate/update/<string:id_>", methods=['PATCH'])
def update_candidate(id_):
    candidate = request.get_json()
    response = candidate_controller.update(id_, candidate)
    return response, 201


@candidate_blueprints.route("/candidate/delete/<string:id_>", methods=['DELETE'])
def delete_candidate(id_):
    response = candidate_controller.delete(id_)
    return response, 204


@candidate_blueprints.route("/candidate/<string:candidate_id>/party/<string:party_id>", methods=['PATCH'])
def assign_party(candidate_id, party_id):
    response = candidate_controller.party_assign(candidate_id, party_id)
    return response, 201

