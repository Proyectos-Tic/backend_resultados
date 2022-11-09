from flask import Blueprint, request

from controllers.votos_controller import VotosController

votos_blueprint = Blueprint('votos_blueprint', __name__)
votos_controller = VotosController()

@votos_blueprint.route("/voto/all", methods=["GET"])
def get_all_votes():
    response = votos_controller.index()
    return response, 200

@votos_blueprint.route("/voto/<string:id>", methods=["GET"])
def get_vote_by_id(id):
    response = votos_controller.show(id)
    return response, 200

@votos_blueprint.route("/voto/create/mesa/<string:mesa_id>/candidato/<string:candidato_id>", methods=["POST"])
def create_vote(mesa_id, candidato_id):
    response = votos_controller.create(mesa_id, candidato_id)
    return response, 201

@votos_blueprint.route("/voto/update/<string:id>", methods=["PATCH"])
def update_vote(id):
    vote = request.get_json()
    response = votos_controller.update(id, vote)
    return response, 201

@votos_blueprint.route("/voto/delete/<string:id>", methods=["DELETE"])
def delete_vote(id):
    response = votos_controller.delete(id)
    return response, 204